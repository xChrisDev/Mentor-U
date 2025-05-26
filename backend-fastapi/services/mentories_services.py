from sqlmodel import Session, select
from core.database import engine
from models.mentor_model import Mentory, Mentor
from models.student_model import Student
from models.mentory_students_link import MentoryStudentLink
from fastapi import UploadFile
import cloudinary
import cloudinary.uploader


def get_all_mentories(student_id: int):
    with Session(engine) as session:
        mentories = session.exec(select(Mentory)).all()
        mentorie_list = []

        for mentory in mentories:
            mentor = session.exec(
                select(Mentor).where(Mentor.id == mentory.id_mentor)
            ).first()

            is_enrolled = (
                session.exec(
                    select(MentoryStudentLink).where(
                        (MentoryStudentLink.student_id == student_id)
                        & (MentoryStudentLink.mentory_id == mentory.id)
                    )
                ).first()
                is not None
            )

            mentorie_list.append(
                {
                    "id": mentory.id,
                    "title": mentory.title,
                    "description": mentory.description,
                    "image": mentory.image,
                    "price": mentory.price,
                    "duration": mentory.duration,
                    "max_students": mentory.max_students,
                    "id_mentor": mentory.id_mentor,
                    "is_enrolled": is_enrolled,
                    "mentor": (
                        {
                            "id": mentor.id,
                            "name": mentor.name,
                            "surname": mentor.surname,
                            "profile_picture": mentor.profile_picture,
                            "specialization": mentor.specialization,
                        }
                        if mentor
                        else None
                    ),
                }
            )

        return mentorie_list

def get_mentories_by_student_id(student_id: int):
    with Session(engine) as session:
        # Obtener todas las mentorías donde el estudiante está inscrito
        mentories = session.exec(
            select(Mentory)
            .join(MentoryStudentLink, Mentory.id == MentoryStudentLink.mentory_id)
            .where(MentoryStudentLink.student_id == student_id)
        ).all()

        mentorie_list = []

        for mentory in mentories:
            # Obtener los datos del mentor
            mentor = session.exec(
                select(Mentor).where(Mentor.id == mentory.id_mentor)
            ).first()

            # Obtener el vínculo del estudiante con la mentoría
            link = session.exec(
                select(MentoryStudentLink).where(
                    (MentoryStudentLink.student_id == student_id)
                    & (MentoryStudentLink.mentory_id == mentory.id)
                )
            ).first()

            mentorie_list.append(
                {
                    "id": mentory.id,
                    "title": mentory.title,
                    "description": mentory.description,
                    "image": mentory.image,
                    "price": mentory.price,
                    "duration": mentory.duration,
                    "max_students": mentory.max_students,
                    "id_mentor": mentory.id_mentor,
                    "mentor": (
                        {
                            "id": mentor.id,
                            "name": mentor.name,
                            "surname": mentor.surname,
                            "profile_picture": mentor.profile_picture,
                            "specialization": mentor.specialization,
                        }
                        if mentor
                        else None
                    ),
                    "progress": link.progress if link else 0,
                    "status": link.status if link else "pendiente",
                }
            )

        return mentorie_list


def register_in_mentory(mentory_id: int, student_id: int):
    with Session(engine) as session:
        enroll = MentoryStudentLink(
            mentory_id=mentory_id,
            student_id=student_id,
            progress=0,
            status="not_started",
        )
        session.add(enroll)
        session.flush()

        session.commit()

        return {"message": "Te inscribiste correctamente"}


def get_mentories_by_id(mentor_id: int):
    with Session(engine) as session:
        mentories = session.exec(
            select(Mentory).where(Mentory.id_mentor == mentor_id)
        ).all()
        if not mentories:
            return {"message": "No hay mentorias registradas"}
        return mentories


def get_mentorie_by_id_mentory(mentory_id: int):
    with Session(engine) as session:
        mentorie = session.exec(select(Mentory).where(Mentory.id == mentory_id)).first()
        if not mentorie:
            return {"message": "No hay mentoria registrada con esa ID"}
        return mentorie


def get_mentorie_by_id(mentory_id: int, student_id: int):
    with Session(engine) as session:
        mentorie = session.get(Mentory, mentory_id)

        if not mentorie:
            return {"message": "Mentoría no encontrada"}

        mentor = session.exec(
            select(Mentor).where(Mentor.id == mentorie.id_mentor)
        ).first()

        link = session.exec(
            select(MentoryStudentLink).where(
                (MentoryStudentLink.student_id == student_id)
                & (MentoryStudentLink.mentory_id == mentory_id)
            )
        ).first()

        return {
            "id": mentorie.id,
            "title": mentorie.title,
            "description": mentorie.description,
            "image": mentorie.image,
            "price": mentorie.price,
            "duration": mentorie.duration,
            "max_students": mentorie.max_students,
            "id_mentor": mentorie.id_mentor,
            "mentor": (
                {
                    "id": mentor.id,
                    "name": mentor.name,
                    "surname": mentor.surname,
                    "profile_picture": mentor.profile_picture,
                    "specialization": mentor.specialization,
                }
                if mentor
                else None
            ),
            "progress": link.progress if link else 0,
            "status": link.status if link else "pendiente",
        }


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
            return {"message": "Mentoría no encontrada"}

        if (
            not title
            or not description
            or price is None
            or duration is None
            or max_students is None
        ):
            return {"message": "Todos los campos son obligatorios"}

        mentory.title = title
        mentory.description = description
        mentory.price = price
        mentory.duration = duration
        mentory.max_students = max_students

        if image:
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
                mentory.image = upload_result["secure_url"]
            except Exception as e:
                return {"message": f"Error al subir imagen: {str(e)}"}

        session.commit()

        return {
            "message": "Mentoría actualizada correctamente",
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
