from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime, timezone
from sqlalchemy import Text, Column, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.problem_model import Problem
    from models.student_model import Student
    from models.mentor_model import Mentory


class StudentSolution(SQLModel, table=True):
    __tablename__ = "student_solutions"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    problem_id: int = Field(
        sa_column=Column(
            "problem_id",
            ForeignKey("problems.id", ondelete="CASCADE"),
        )
    )
    
    student_id: int = Field(
        sa_column=Column(
            "student_id",
            ForeignKey("students.id", ondelete="CASCADE"),
        )
    )
    
    mentorie_id: int = Field(
        sa_column=Column(
            "mentorie_id",
            ForeignKey("mentories.id", ondelete="CASCADE"),
        )
    )
    
    code: str = Field(sa_column=Column(Text))
    comments: Optional[str] = Field(sa_column=Column(Text), default="")
    result: str = Field(nullable=False) 
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    # Relaciones
    problem: Optional["Problem"] = Relationship()
    student: Optional["Student"] = Relationship()
    mentory: Optional["Mentory"] = Relationship()


# Modelo para respuesta con información completa
class StudentSolutionWithDetails(SQLModel):
    id: int
    problem_id: int
    student_id: int
    mentorie_id: int
    code: str
    comments: Optional[str]
    result: str
    created_at: datetime
    updated_at: datetime
    
    problem_title: str
    problem_description: str
    problem_difficulty: str
    problem_topic: str
    
    student_name: str
    student_surname: str
    
    mentorie_title: str
    mentorie_description: str


class StudentSolutionCreate(SQLModel):
    problem_id: int
    student_id: int
    mentorie_id: int
    code: str
    comments: Optional[str] = ""
    result: str


class StudentSolutionUpdate(SQLModel):
    code: Optional[str] = None
    comments: Optional[str] = None
    result: Optional[str] = None