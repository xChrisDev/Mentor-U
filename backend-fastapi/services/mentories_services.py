from sqlmodel import Session, select
from core.database import engine
from models.mentor_model import Mentory
from fastapi import UploadFile
import cloudinary
import cloudinary.uploader


def get_all_mentories():
    with Session(engine) as session:
        mentories = session.exec(select(Mentory))
        mentorie_list = []
        for mentorie in mentories:
            mentorie_list.append(mentorie)
        return mentorie_list


def get_mentories_by_id(mentor_id: int):
    with Session(engine) as session:
        mentories = session.exec(select(Mentory).where(Mentory.id_mentor == mentor_id)).all()
        if not mentories:
            return {"message": "No hay mentorias registradas"}
        return mentories
    
def get_mentorie_by_id(mentory_id: int):
    with Session(engine) as session:
        mentorie = session.get(Mentory, mentory_id)
        if not mentorie:
            return {"message": "Mentoria no encontrado"}
        return mentorie


async def create_mentorie_service(
    id_mentor: int,
    title: str,
    description: str,
    price: float,
    duration: int,
    max_students: int,
    image: UploadFile,
):
    if not title or not description or not price or not duration or not max_students:
        return {"message": "Todos los campos son obligatorios"}

    if not image.content_type.startswith("image/"):
        return {"message": "Solo se permiten archivos de imagen"}

    try:
        file_bytes = await image.read()
        upload_result = cloudinary.uploader.upload(
            file_bytes,
            folder="mentor_u/mentories_pictures",
            public_id=f"{id_mentor}_{title}",
            overwrite=True,
            resource_type="image",
        )
    except Exception as e:
        return {"message": f"Error al subir imagen: {str(e)}"}

    profile_picture_url = upload_result["secure_url"]

    with Session(engine) as session:
        new_mentory = Mentory(
            title=title,
            description=description,
            price=price,
            duration=duration,
            max_students=max_students,
            image=profile_picture_url,
            id_mentor=id_mentor,
        )
        session.add(new_mentory)
        session.flush()

        session.commit()

        return {
            "message": "Mentoria registrada correctamente",
            "mentor_id": new_mentory.id,
            "profile_picture": profile_picture_url,
        }


async def update_mentorie_service(
    mentory_id: int,
    id_mentor: int,
    title: str,
    description: str,
    price: float,
    duration: int,
    max_students: int,
    image: UploadFile = None,
):
    with Session(engine) as session:
        mentory = session.get(Mentory, mentory_id)
        if not mentory:
            return {"message": "Mentoria no encontrado"}

        if (
            not title
            or not description
            or not price
            or not duration
            or not max_students
        ):
            return {"message": "Todos los campos son obligatorios"}

        if not image.content_type.startswith("image/"):
            return {"message": "Solo se permiten archivos de imagen"}

        mentory.title = title
        mentory.description = description
        mentory.price = price
        mentory.duration = duration
        mentory.max_students = max_students

        if image:
            try:
                file_bytes = await image.read()
                upload_result = cloudinary.uploader.upload(
                    file_bytes,
                    folder="mentor_u/mentories_pictures",
                    public_id=f"{id_mentor}_{title}",
                    overwrite=True,
                    resource_type="image",
                )
                mentory.image = upload_result["secure_url"]
            except Exception as e:
                return {"message": f"Error al subir imagen: {str(e)}"}

        session.commit()

        return {
            "message": "Mentoria actualizado correctamente",
            "mentor_id": mentory.id,
            "profile_picture": mentory.image,
        }


def delete_mentorie_service(mentory_id: int):
    with Session(engine) as session:
        statement = select(Mentory).where(Mentory.id == mentory_id)
        mentory = session.exec(statement).first()
        if not mentory:
            return {"message": "Mentoria no encontrado"}
        session.delete(mentory)
        session.commit()
        return {"message": "Mentoria eliminado correctamente"}
