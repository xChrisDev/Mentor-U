from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import List, Optional
from services.mentor_services import (
    create_mentor_service,
    update_mentor_service,
    delete_mentor_service,
    get_mentor_by_id,
    get_all_mentors,
)

router = APIRouter(prefix="/api/mentors", tags=["Mentors"])

@router.post("/create")
async def post_mentor(
    user_id: int = Form(...),
    name: str = Form(...),
    surname: str = Form(...),
    biography: str = Form(...),
    specialization: str = Form(...),
    genre: str = Form(...),
    technologies_ids: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        technologies_ids_list = [int(id.strip()) for id in technologies_ids.split(',')]
    except ValueError:
        raise HTTPException(status_code=400, detail="IDs de tecnologías inválidos (usa solo números separados por comas)")

    result = await create_mentor_service(
        user_id=user_id,
        name=name,
        surname=surname,
        biography=biography,
        specialization=specialization,
        genre=genre,
        technologies_ids=technologies_ids_list,
        file=file
    )
    return result

@router.put("/update/{mentor_id}")
async def put_mentor(
    mentor_id: int,
    user_id: int = Form(...),
    name: str = Form(...),
    surname: str = Form(...),
    biography: str = Form(...),
    specialization: str = Form(...),
    genre: str = Form(...),
    technologies_ids: str = Form(...),
    file: Optional[UploadFile] = File(None)
):
    try:
        technologies_ids_list = [int(id.strip()) for id in technologies_ids.split(',')]
    except ValueError:
        raise HTTPException(status_code=400, detail="IDs de tecnologías inválidos")

    result = await update_mentor_service(
        mentor_id=mentor_id,
        user_id=user_id,
        name=name,
        surname=surname,
        biography=biography,
        specialization=specialization,
        genre=genre,
        technologies_ids=technologies_ids_list,
        file=file
    )
    return result

@router.delete("/delete/{mentor_id}")
def delete_mentor(mentor_id: int):
    return delete_mentor_service(mentor_id)

@router.get("/get/{mentor_id}")
def get_mentor(mentor_id: int):
    return get_mentor_by_id(mentor_id)

@router.get("/all")
def get_all():
    return get_all_mentors()
