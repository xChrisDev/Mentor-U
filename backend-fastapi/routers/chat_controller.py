from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException
from sqlmodel import Session
from jose import JWTError
from models.user_model import User
from models.message_model import Message
from services.connection_manager import ConnectionManager
from auth.jwt import get_current_user_from_token
from core.database import engine

router = APIRouter(prefix="/api/chat", tags=["Chats"])
manager = ConnectionManager()

@router.websocket("/ws/private")
async def private_chat(websocket: WebSocket):
    token = websocket.query_params.get("token")
    if not token:
        await websocket.close()
        return
    try:
        user: User = get_current_user_from_token(token)
    except JWTError:
        await websocket.close()
        return

    await manager.connect(user.id, websocket)

    try:
        while True:
            # Espera un JSON con { "to_user_id": 2, "message": "Hola" }
            data = await websocket.receive_json()
            to_user_id = data["to_user_id"]
            message = data["message"]

            if not message or not message.strip():
                await websocket.send_text("El mensaje no puede estar vacío.")
                continue

            new_message = Message(
                from_user_id=user.id,
                to_user_id=to_user_id,
                content=message
            )

            with Session(engine) as session:
                session.add(new_message)
                session.commit()

            await manager.send_private_message(f"{user.username}: {message}", to_user_id)
    except WebSocketDisconnect:
        manager.disconnect(user.id)


@router.delete("/{message_id}")
async def delete_message(message_id: int):
    with Session(engine) as session:
        msg = session.get(Message, message_id)
        if msg:
            session.delete(msg)
            session.commit()
            return {"status": "deleted", "message_id": message_id}
        raise HTTPException(status_code=404, detail="Mensaje no encontrado")
