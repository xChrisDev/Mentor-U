from fastapi import APIRouter, UploadFile, File, Form
from services.mentories_services import (
    create_mentorie_service,
    update_mentorie_service,
    delete_mentorie_service,
    get_mentories_by_id,
    get_mentorie_by_id,
    get_all_mentories,
)

router = APIRouter(prefix="/api/mentories", tags=["Mentories"])


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
    mentor_id: int = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    price: str = Form(...),
    duration: str = Form(...),
    max_students: str = Form(...),
    image: UploadFile = File(...),
):
    result = await update_mentorie_service(
        mentory_id=mentory_id,
        mentor_id=mentor_id,
        title=title,
        description=description,
        price=price,
        duration=duration,
        max_students=max_students,
        image=image,
    )
    return result


@router.delete("/delete/{mentory_id}")
def delete_mentory(mentory_id: int):
    return delete_mentorie_service(mentory_id)


@router.get("/get/{mentor_id}")
def get_mentories(mentor_id: int):
    return get_mentories_by_id(mentor_id)

@router.get("/get/mentorie/{mentory_id}")
def get_mentory(mentory_id: int):
    return get_mentorie_by_id(mentory_id)

@router.get("/all")
def get_all():
    return get_all_mentories()
