from sqlmodel import SQLModel, Field
from typing import Optional

class MentoryStudentLink(SQLModel, table=True):
    __tablename__ = "mentory_students_link"
    mentory_id: Optional[int] = Field(
        default=None, foreign_key="mentories.id", primary_key=True
    )
    student_id: Optional[int] = Field(
        default=None, foreign_key="students.id", primary_key=True
    )
    progress: int = Field(index=True, nullable=False)
    status: str = Field(index=True, nullable=False)
    
