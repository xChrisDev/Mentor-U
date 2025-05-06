from pydantic import BaseModel
from typing import List

class ProblemCreate(BaseModel):
    topic: str
    level: str
    lang: str
    
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
    examples: List[Example]

    class Config:
        orm_mode = True