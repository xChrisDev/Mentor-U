from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Enum as SQLAlchemyEnum
from models.enums.constants import GenreEnum
from models.mentor_model import Mentory
from models.mentory_students_link import MentoryStudentLink


class Student(SQLModel, table=True):
    __tablename__ = "students"

    id: Optional[int] = Field(default=None, primary_key=True)
    
    # CASCADE: Si se elimina un usuario, su perfil de estudiante también se elimina
    user_id: int = Field(
        sa_column=Column(
            "user_id",
            ForeignKey("users.id", ondelete="CASCADE"),
            unique=True,
            nullable=False
        )
    )
    
    name: str = Field(index=True, nullable=False)
    surname: str = Field(index=True, nullable=False)
    profile_picture: str = Field(nullable=False)

    genre: GenreEnum = Field(
        sa_column=Column(SQLAlchemyEnum(GenreEnum), nullable=False),
        description="Género del estudiante",
    )

    mentories: List["Mentory"] = Relationship(
        back_populates="students", link_model=MentoryStudentLink
    )


Student.user = Relationship(back_populates="student")