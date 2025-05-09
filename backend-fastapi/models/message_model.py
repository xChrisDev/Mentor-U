from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime, timezone 

class Message(SQLModel, table=True):
    __tablename__ = "messages"
    id: Optional[int] = Field(default=None, primary_key=True)
    from_user_id: int = Field(foreign_key="users.id")
    to_user_id: int = Field(foreign_key="users.id")
    content: Optional[str] = Field(default=None, nullable=False) 
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
