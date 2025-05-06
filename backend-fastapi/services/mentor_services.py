from sqlmodel import Session, select
from core.database import engine
from models.mentor_model import Mentor, MentorTechnologyLink
from models.enums.constants import GenreEnum
from fastapi import UploadFile
from models.user_model import User
from typing import List
from sqlalchemy import delete
import cloudinary
import cloudinary.uploader


def get_all_mentors():
    with Session(engine) as session:
        mentors = session.exec(select(Mentor).all())
        mentor_list = []
        for mentor in mentors:
            user = session.get(User, mentor.user_id)
            mentor_list.append({"mentor": mentor, "user": user})
        return mentor_list


def get_mentor_by_id(mentor_id: int):
    with Session(engine) as session:
        mentor = session.get(Mentor, mentor_id)
        if not mentor:
            return {"message": "Mentor no encontrado"}

        user = session.get(User, mentor.user_id)
        return {"mentor": mentor, "user": user}


async def create_mentor_service(
    user_id: int,
    name: str,
    surname: str,
    biography: str,
    specialization: str,
    genre: str,
    technologies_ids: List[int],
    file: UploadFile,
):
    if not name or not surname or not biography or not specialization or not genre:
        return {"message": "Todos los campos son obligatorios"}

    try:
        genre_enum = GenreEnum(genre)
    except ValueError:
        return {"message": "Género no válido"}

    if not file.content_type.startswith("image/"):
        return {"message": "Solo se permiten archivos de imagen"}

    try:
        file_bytes = await file.read()
        upload_result = cloudinary.uploader.upload(
            file_bytes,
            folder="mentor_u/profile_pictures",
            public_id=f"{user_id}_{name}_{surname}",
            overwrite=True,
            resource_type="image",
        )
    except Exception as e:
        return {"message": f"Error al subir imagen: {str(e)}"}

    profile_picture_url = upload_result["secure_url"]

    with Session(engine) as session:
        new_mentor = Mentor(
            user_id=user_id,
            name=name,
            surname=surname,
            biography=biography,
            specialization=specialization,
            genre=genre_enum,
            profile_picture=profile_picture_url,
        )
        session.add(new_mentor)
        session.flush()

        for tech_id in technologies_ids:
            link = MentorTechnologyLink(mentor_id=new_mentor.id, technology_id=tech_id)
            session.add(link)

        session.commit()

        return {
            "message": "Mentor registrado correctamente",
            "mentor_id": new_mentor.id,
            "profile_picture": profile_picture_url,
        }


async def update_mentor_service(
    mentor_id: int,
    user_id: int,
    name: str,
    surname: str,
    biography: str,
    specialization: str,
    genre: str,
    technologies_ids: List[int],
    file: UploadFile = None,
):
    with Session(engine) as session:
        mentor = session.get(Mentor, mentor_id)
        if not mentor:
            return {"message": "Mentor no encontrado"}

        if not name or not surname or not biography or not specialization or not genre:
            return {"message": "Todos los campos son obligatorios"}

        try:
            genre_enum = GenreEnum(genre)
        except ValueError:
            return {"message": "Género no válido"}

        mentor.name = name
        mentor.surname = surname
        mentor.biography = biography
        mentor.specialization = specialization
        mentor.genre = genre_enum

        if file:
            try:
                file_bytes = await file.read()
                upload_result = cloudinary.uploader.upload(
                    file_bytes,
                    folder="mentor_u/profile_pictures",
                    public_id=f"{user_id}_{name}_{surname}",
                    overwrite=True,
                    resource_type="image",
                )
                mentor.profile_picture = upload_result["secure_url"]
            except Exception as e:
                return {"message": f"Error al subir imagen: {str(e)}"}

        stmt = delete(MentorTechnologyLink).where(
            MentorTechnologyLink.mentor_id == mentor.id
        )
        session.exec(stmt)
        for tech_id in technologies_ids:
            link = MentorTechnologyLink(mentor_id=mentor.id, technology_id=tech_id)
            session.add(link)

        session.commit()

        return {
            "message": "Mentor actualizado correctamente",
            "mentor_id": mentor.id,
            "profile_picture": mentor.profile_picture,
        }


def delete_mentor_service(mentor_id: int):
    with Session(engine) as session:
        statement = select(Mentor).where(Mentor.id == mentor_id)
        mentor = session.exec(statement).first()
        if not mentor:
            return {"message": "Mentor no encontrado"}
        session.delete(mentor)
        session.commit()
        return {"message": "Mentor eliminado correctamente"}
