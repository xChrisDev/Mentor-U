from sqlmodel import SQLModel, Field
from typing import Optional
from sqlalchemy import Column, ForeignKey

class StudentProblemLink(SQLModel, table=True):
    __tablename__ = "student_problems_link"
    problem_id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            "problem_id",
            ForeignKey("problems.id", ondelete="CASCADE"),
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
    status: str = Field(index=True, nullable=False)