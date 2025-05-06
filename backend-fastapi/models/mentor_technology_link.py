from sqlmodel import SQLModel, Field
from typing import Optional

class MentorTechnologyLink(SQLModel, table=True):
    __tablename__ = "mentor_technology_link"
    mentor_id: Optional[int] = Field(
        default=None, foreign_key="mentors.id", primary_key=True
    )
    technology_id: Optional[int] = Field(
        default=None, foreign_key="technologies.id", primary_key=True
    )
