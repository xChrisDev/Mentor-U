from sqlmodel import Session, select
from core.database import engine
from models.student_model import Student
from models.enums.constants import GenreEnum
from fastapi import UploadFile
from models.user_model import User
import cloudinary
import cloudinary.uploader


def get_all_students():
    with Session(engine) as session:
        students = session.exec(select(Student))
        student_list = []
        for student in students:
            user = session.get(User, student.user_id)
            student_list.append({"student": student, "user": user.username})
        return student_list


def get_student_by_id(student_id: int):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if not student:
            return {"message": "Estudiante no encontrado"}

        user = session.get(User, student.user_id)
        return {"student": student, "user": user.username}


async def create_student_service(
    user_id: int,
    name: str,
    surname: str,
    genre: str,
    file: UploadFile,
):
    if not name or not surname or not genre:
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
        new_student = Student(
            user_id=user_id,
            name=name,
            surname=surname,
            genre=genre_enum,
            profile_picture=profile_picture_url,
        )
        session.add(new_student)
        session.flush()
        session.commit()

        return {
            "message": "Estudiante registrado correctamente",
            "student_id": new_student.id,
            "profile_picture": profile_picture_url,
        }


async def update_student_service(
    student_id: int,
    user_id: int,
    name: str,
    surname: str,
    genre: str,
    file: UploadFile = None,
):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if not student:
            return {"message": "Estudiante no encontrado"}

        if not name or not surname or not genre:
            return {"message": "Todos los campos son obligatorios"}

        try:
            genre_enum = GenreEnum(genre)
        except ValueError:
            return {"message": "Género no válido"}

        student.name = name
        student.surname = surname
        student.genre = genre_enum

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
                student.profile_picture = upload_result["secure_url"]
            except Exception as e:
                return {"message": f"Error al subir imagen: {str(e)}"}

        session.commit()

        return {
            "message": "Estudiante actualizado correctamente",
            "student_id": student.id,
            "profile_picture": student.profile_picture,
        }


def delete_student_service(student_id: int):
    with Session(engine) as session:
        statement = select(student).where(student.id == student_id)
        student = session.exec(statement).first()
        if not student:
            return {"message": "Estudiante no encontrado"}
        session.delete(student)
        session.commit()
        return {"message": "Estudiante eliminado correctamente"}
