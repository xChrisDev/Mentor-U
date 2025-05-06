from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from models.enums.constants import RoleEnum

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, nullable=False)
    email: str = Field(index=True, unique=True, nullable=False)
    password: str = Field(nullable=False)
    role: RoleEnum = Field(..., description="Tipo de usuario")

User.mentor = Relationship(back_populates="user")
User.student = Relationship(back_populates="user")
