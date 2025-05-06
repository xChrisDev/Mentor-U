from sqlmodel import Session, select
from core.database import engine
from models.user_model import User
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
            return {
                "message": "La contraseña debe tener al menos 8 caracteres"
            }

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
