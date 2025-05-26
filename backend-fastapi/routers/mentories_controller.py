from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional
from schemas.mentorie_scheme import MentorieStudentLink
from services.mentories_services import (
    create_mentorie_service,
    update_mentorie_service,
    delete_mentorie_service,
    get_mentories_by_id,
    get_mentorie_by_id,
    get_all_mentories,
    register_in_mentory,
    get_mentories_by_student_id,
    get_students_count,
    get_mentorie_by_id_mentory
)

router = APIRouter(prefix="/api/mentories", tags=["Mentories"])


@router.post("/enroll")
def enroll_student(data: MentorieStudentLink):
    return register_in_mentory(data.mentory_id, data.student_id)


@router.post("/create")
async def post_mentory(
    id_mentor: int = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    duration: int = Form(...),
    max_students: int = Form(...),
    image: UploadFile = File(...),
):

    result = await create_mentorie_service(
        id_mentor=id_mentor,
        title=title,
        description=description,
        price=price,
        duration=duration,
        max_students=max_students,
        image=image,
    )
    return result


@router.put("/update/{mentory_id}")
async def put_mentory(
    mentory_id: int,
    id_mentor: int = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    price: str = Form(...),
    duration: str = Form(...),
    max_students: str = Form(...),
    image: Optional[UploadFile] = File(None),
):
    result = await update_mentorie_service(
        mentory_id=mentory_id,
        id_mentor=id_mentor,
        title=title,
        description=description,
        price=float(price),
        duration=int(duration),
        max_students=int(max_students),
        image=image,
    )
    return result


@router.delete("/delete/{mentory_id}")
def delete_mentory(mentory_id: int):
    return delete_mentorie_service(mentory_id)


@router.get("/get/{mentor_id}")
def get_mentories(mentor_id: int):
    return get_mentories_by_id(mentor_id)

@router.get("/get/mentorie/{mentorie_id}")
def get_mentories(mentorie_id: int):
    return get_mentorie_by_id_mentory(mentorie_id)

@router.get("/get/mentorie/{mentory_id}/{student_id}")
def get_mentory(mentory_id: int, student_id: int):
    return get_mentorie_by_id(mentory_id, student_id)

@router.get("/all/{student_id}")
def get_all(student_id: int):
    return get_all_mentories(student_id)

@router.get("/{student_id}")
def get_student_mentories(student_id: int):
    return get_mentories_by_student_id(student_id)

@router.get("/{mentor_id}/count")
def get_student_count_mentory(mentor_id: int):
    return get_students_count(mentor_id)
