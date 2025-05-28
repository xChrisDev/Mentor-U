from pydantic import BaseModel
from typing import List, Optional

class ProblemStatus(BaseModel):
    problem_id: int
    student_id: int
    
class ProblemProgress(BaseModel):
    mentory_id: int
    student_id: int
    
class ProblemStatusUpdate(BaseModel):
    problem_id: int
    student_id: int
    status: str

class ProblemCreate(BaseModel):
    topic: str
    level: str
    lang: str
    id_mentor: int
    id_mentorie: int
    
class Example(BaseModel):
    input: str
    output: str
    explanation: str

    class Config:
        orm_mode = True

class ProblemWithExamples(BaseModel):
    id: int
    title: str
    description: str
    difficulty: str
    constraints: str
    solution: str
    topic: str
    lang: str
    id_mentor: int
    id_mentorie: int
    examples: List[Example]

    class Config:
        orm_mode = True
        
        
class PromptRequest(BaseModel):
    lang: str
    code: str
    examples: List[Example]
