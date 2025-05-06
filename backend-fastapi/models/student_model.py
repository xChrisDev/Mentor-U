from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from sqlalchemy import Column
from sqlalchemy import Enum as SQLAlchemyEnum
from models.enums.constants import GenreEnum

class Student(SQLModel, table=True):
    __tablename__ = "students"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", unique=True, nullable=False)
    name: str = Field(index=True, nullable=False)
    surname: str = Field(index=True, nullable=False)
    profile_picture: str = Field(nullable=False)

    genre: GenreEnum = Field(
        sa_column=Column(SQLAlchemyEnum(GenreEnum), nullable=False),
        description="Género del estudiante",
    )

Student.user = Relationship(back_populates="student")
