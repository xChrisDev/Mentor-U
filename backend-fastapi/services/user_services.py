from sqlmodel import Session, select
from core.database import engine
from models.user_model import User
from models.mentor_model import Mentor
from models.student_model import Student
from auth.jwt import hash_password, verify_password, create_access_token
from email_validator import validate_email, EmailNotValidError
from sqlalchemy import or_


def register_user(username: str, password: str, email: str, role: str):
    with Session(engine) as session:
        existing_user = session.exec(
            select(User).where(or_(User.username == username, User.email == email))
        ).first()

        if existing_user:
            return {"message": "Usuario ya existe"}

        if email:
            try:
                valid = validate_email(email)
                email = valid.email
            except EmailNotValidError as e:
                return {"message": "Email no válido"}

        if not username or not password or not email or not role:
            return {"message": "Todos los campos son obligatorios"}

        if len(password) < 8:
            return {"message": "La contraseña debe tener al menos 8 caracteres"}

        user = User(
            username=username, email=email, role=role, password=hash_password(password)
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return {"message": "Usuario creado correctamente", "user": user.username}


def login_user(username: str, password: str):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.username == username)).first()
        if not user or not verify_password(password, user.password):
            return None
        return create_access_token(data={"sub": user.username})


def get_role_by_user(username: str):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.username == username)).first()
        if not user:
            return None

        mentor = session.exec(select(Mentor).where(Mentor.user_id == user.id)).first()
        if mentor:
            return {"role": user.role, "data": mentor}

        student = session.exec(select(Student).where(Student.user_id == user.id)).first()
        if student:
            return {"role": user.role, "data": student}

        return None
    
def delete_user(user_id: int):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).first()
        if not user:
            return {"message": "Usuario no encontrado"}
        session.delete(user)
        session.commit()
        return {"message": "Cuenta eliminada correctamente"}


def update_user(id: int, username: str, password: str, email: str, role: str):
    with Session(engine) as session:
        user = session.get(User, id)
        if not user:
            return {"message": "Error al encontrar usuario"}

        if email:
            try:
                valid = validate_email(email)
                email = valid.email
            except EmailNotValidError as e:
                return {"message": "Email no válido"}

        if not username or not password or not email or not role:
            return {"message": "Todos los campos son obligatorios"}

        if len(password) < 8:
            return {"message": "La contraseña debe tener al menos 8 caracteres"}

        new_user = User(
            username=username, email=email, role=role, password=hash_password(password)
        )

        existing_user = session.exec(
            select(User).where(
                or_(User.username == new_user.username, User.email == new_user.email)
            )
        ).first()

        if existing_user:
            return {"message": "El nombre de usuario o email ya está en uso"}

        user.username = new_user.username
        user.passwrod = new_user.password
        user.email = new_user.email

        session.commit()

        return {"message": "Usuario actualizado correctamente"}
