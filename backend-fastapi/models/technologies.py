from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from models.mentor_technology_link import MentorTechnologyLink
from models.mentor_model import Mentor

class Technologies(SQLModel, table=True):
    __tablename__ = "technologies"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    mentors: List[Mentor] = Relationship(
        back_populates="technologies", link_model=MentorTechnologyLink
    )
