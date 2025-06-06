from pydantic import BaseModel

class MentoriesCreate(BaseModel):
    title: str
    description: str
    image: str
    price: float
    duration: int
    max_students: int
    id_mentor: int

class MentorieStudentLink(BaseModel):
    mentory_id: int
    student_id: int
    progress: int
    status: str