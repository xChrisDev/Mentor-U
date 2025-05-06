from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from sqlalchemy import Text, Column
from sqlalchemy import Enum as SQLAlchemyEnum
from models.enums.constants import GenreEnum
from models.mentor_technology_link import MentorTechnologyLink

class Mentor(SQLModel, table=True):
    __tablename__ = "mentors"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", unique=True, nullable=False)

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

from models.technologies import Technologies

Mentor.user = Relationship(back_populates="mentor")
