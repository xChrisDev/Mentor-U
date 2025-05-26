from sqlmodel import SQLModel, Field
from typing import Optional
from sqlalchemy import Column, ForeignKey

class MentorTechnologyLink(SQLModel, table=True):
    __tablename__ = "mentor_technology_link"
    mentor_id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            "mentor_id",
            ForeignKey("mentors.id", ondelete="CASCADE"),
            primary_key=True
        )
    )
    technology_id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            "technology_id", 
            ForeignKey("technologies.id", ondelete="CASCADE"),
            primary_key=True
        )
    )