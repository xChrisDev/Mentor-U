from fastapi import APIRouter, HTTPException, Response, Request
from schemas.user_scheme import UserCreate, UserLogin, Token
from services.user_services import (
    get_role_by_user,
    register_user,
    login_user,
    update_user,
    delete_user,
)

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.post("/register")
def register(user: UserCreate):
    response = register_user(user.username, user.password, user.email, user.role)
    if not response:
        raise HTTPException(status_code=500, detail="Error al crear el usuario")
    return response

@router.get("/me")
def get_logged_user(request: Request):
    username = request.cookies.get("session_username")
    if not username:
        raise HTTPException(status_code=401, detail="Usuario no autenticado")

    response = get_role_by_user(username)
    if not response:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return response


@router.post("/login")
def login(user: UserLogin, response: Response):
    result = login_user(user.username, user.password)
    if not result:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    response.set_cookie(
        key="session_username",
        value=result["username"],
        httponly=True,
        secure=False,  # True en producción con HTTPS
        samesite="Lax"
    )

    return {"message": result["message"], "user": result["username"]}


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("session_username")
    return {"message": "Sesión cerrada correctamente"}


@router.put("/update/{id_user}")
def update_account(id_user: int, user: UserCreate):
    response = update_user(id_user, user.username, user.password, user.email, user.role)
    if not response:
        raise HTTPException(status_code=500, detail="Error al actualizar el usuario")
    return response


@router.delete("/delete/{id_user}")
def delete_account(id_user: int):
    response = delete_user(id_user)
    if not response:
        raise HTTPException(status_code=500, detail="Error al elimiar la cuenta")
    return response


@router.get("/get_user_data/{username}")
def register(username):
    response = get_role_by_user(username)
    if not response:
        raise HTTPException(
            status_code=500, detail="Error al obtener la información del usuario"
        )
    return response
