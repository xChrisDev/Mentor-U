from pydantic import BaseModel
from typing import List
from models.enums.constants import GenreEnum


class MentorCreate(BaseModel):
    name: str
    surname: str
    biography: str
    profile_picture: str
    specialization: str
    genre: GenreEnum
    technologies_ids: List[int]
    user_id: int
