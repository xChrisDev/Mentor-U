from fastapi import APIRouter, HTTPException
from schemas.user_scheme import UserCreate, UserLogin, Token
from services.user_services import register_user, login_user, update_user, delete_user

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.post("/register")
def register(user: UserCreate):
    response = register_user(user.username, user.password, user.email, user.role)
    if not response:
        raise HTTPException(status_code=500, detail="Error al crear el usuario")
    return response


@router.post("/login", response_model=Token)
def login(user: UserLogin):
    token = login_user(user.username, user.password)
    if not token:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"access_token": token, "token_type": "bearer"}


@router.put("/update")
def update_account(id_user: int, user: UserCreate):
    response = update_user(id_user, user.username, user.password, user.email, user.role)
    if not response:
        raise HTTPException(status_code=500, detail="Error al actualizar el usuario")
    return response


@router.delete("/delete")
def delete_account(id_user: int):
    response = delete_user(id_user)
    if not response:
        raise HTTPException(status_code=500, detail="Error al elimiar la cuenta")
    return response
