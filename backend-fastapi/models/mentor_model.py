from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from sqlalchemy import Text, Column, ForeignKey
from sqlalchemy import Enum as SQLAlchemyEnum
from models.enums.constants import GenreEnum
from models.mentor_technology_link import MentorTechnologyLink
from models.mentory_students_link import MentoryStudentLink
from models.student_solution import StudentSolution


class Mentory(SQLModel, table=True):
    __tablename__ = "mentories"
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True, nullable=False)
    description: str = Field(nullable=False)
    image: str = Field(nullable=False)
    price: float = Field(nullable=False)
    duration: int = Field(nullable=False)
    max_students: int = Field(nullable=False)

    # CASCADE: Si se elimina un mentor, sus mentorías también se eliminan
    id_mentor: int = Field(
        sa_column=Column(
            "id_mentor", 
            ForeignKey("mentors.id", ondelete="CASCADE"), 
            nullable=False
        )
    )

    students: List["Student"] = Relationship(
        back_populates="mentories", link_model=MentoryStudentLink
    )
    
    solutions: List["StudentSolution"] = Relationship(back_populates="mentory")


class Mentor(SQLModel, table=True):
    __tablename__ = "mentors"

    id: Optional[int] = Field(default=None, primary_key=True)
    
    # CASCADE: Si se elimina un usuario, su perfil de mentor también se elimina
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
    biography: str = Field(sa_column=Column(Text), default="")
    profile_picture: str = Field(nullable=False)
    specialization: str = Field(nullable=False)

    genre: GenreEnum = Field(
        sa_column=Column(SQLAlchemyEnum(GenreEnum), nullable=False),
        description="Género del mentor",
    )

    technologies: List["Technologies"] = Relationship(
        back_populates="mentors", link_model=MentorTechnologyLink
    )


from models.student_model import Student
from models.technologies import Technologies

Mentor.user = Relationship(back_populates="mentor")