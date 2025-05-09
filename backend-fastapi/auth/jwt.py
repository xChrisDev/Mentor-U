from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import Depends
from sqlmodel import Session, select
from models.user_model import User
from core.database import get_session
from passlib.context import CryptContext
from core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str):
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user_from_token(token: str, session: Session = Depends(get_session)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise JWTError("ID de usuario no presente en el token")
    except JWTError:
        raise JWTError("Token inválido o expirado")

    user = session.exec(select(User).where(User.id == int(user_id))).first()
    if user is None:
        raise JWTError("Usuario no encontrado")
    return user