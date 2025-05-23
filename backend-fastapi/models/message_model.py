from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timezone 
from sqlalchemy import Column, ForeignKey

class Message(SQLModel, table=True):
    __tablename__ = "messages"
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # CASCADE: Si se elimina un usuario, sus mensajes también se eliminan
    from_user_id: int = Field(
        sa_column=Column(
            "from_user_id",
            ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False
        )
    )
    to_user_id: int = Field(
        sa_column=Column(
            "to_user_id",
            ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False
        )
    )
    
    content: Optional[str] = Field(default=None, nullable=False) 
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
