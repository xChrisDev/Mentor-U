from sqlmodel import SQLModel, Field
from typing import Optional

class StudentProblemLink(SQLModel, table=True):
    __tablename__ = "student_problems_link"
    problem_id: Optional[int] = Field(
        default=None, foreign_key="problems.id", primary_key=True
    )
    student_id: Optional[int] = Field(
        default=None, foreign_key="students.id", primary_key=True
    )
    status: str = Field(index=True, nullable=False)
    
