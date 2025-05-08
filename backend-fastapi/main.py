from fastapi import FastAPI
from core.database import create_db
from core.config_cloud import init_cloudinary
from routers import (
    user_controller,
    problem_controller,
    mentor_controller,
    student_controller,
    mentories_controller,
)

app = FastAPI()
create_db()
init_cloudinary()

app.include_router(user_controller.router)
app.include_router(problem_controller.router)
app.include_router(mentor_controller.router)
app.include_router(student_controller.router)
app.include_router(mentories_controller.router)
