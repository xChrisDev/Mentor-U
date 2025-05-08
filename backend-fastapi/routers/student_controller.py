from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import List, Optional
from services.student_services import (
    create_student_service,
    update_student_service,
    delete_student_service,
    get_student_by_id,
    get_all_students,
)

router = APIRouter(prefix="/api/students", tags=["Students"])

@router.post("/create")
async def post_student(
    user_id: int = Form(...),
    name: str = Form(...),
    surname: str = Form(...),
    genre: str = Form(...),
    file: UploadFile = File(...)
):
    result = await create_student_service(
        user_id=user_id,
        name=name,
        surname=surname,
        genre=genre,
        file=file
    )
    return result

@router.put("/update/{student_id}")
async def put_student(
    student_id: int,
    user_id: int = Form(...),
    name: str = Form(...),
    surname: str = Form(...),
    genre: str = Form(...),
    file: Optional[UploadFile] = File(None)
):

    result = await update_student_service(
        student_id=student_id,
        user_id=user_id,
        name=name,
        surname=surname,
        genre=genre,
        file=file
    )
    return result

@router.delete("/delete/{student_id}")
def delete_student(student_id: int):
    return delete_student_service(student_id)

@router.get("/get/{student_id}")
def get_student(student_id: int):
    return get_student_by_id(student_id)

@router.get("/all")
def get_all():
    return get_all_students()
