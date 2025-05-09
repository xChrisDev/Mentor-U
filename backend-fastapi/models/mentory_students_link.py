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
    registered_students: int = Field(nullable=False)
