from sqlmodel import SQLModel, Field
from typing import Optional
from sqlalchemy import Column, ForeignKey

class MentoryStudentLink(SQLModel, table=True):
    __tablename__ = "mentory_students_link"
    mentory_id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            "mentory_id",
            ForeignKey("mentories.id", ondelete="CASCADE"),
            primary_key=True
        )
    )
    student_id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            "student_id",
            ForeignKey("students.id", ondelete="CASCADE"),
            primary_key=True
        )
    )
    progress: int = Field(index=True, nullable=False)
    status: str = Field(index=True, nullable=False)