from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from sqlalchemy import Text, Column


class Example(SQLModel, table=True):
    __tablename__ = "examples"
    id: Optional[int] = Field(default=None, primary_key=True)
    input: str = Field(nullable=False)
    output: str = Field(nullable=False)
    explanation: str = Field(nullable=False)

    problem_id: int = Field(foreign_key="problems.id", nullable=False)
    problem: Optional["Problem"] = Relationship(back_populates="examples")


class Problem(SQLModel, table=True):
    __tablename__ = "problems"
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True, nullable=False)
    description: str = Field(sa_column=Column(Text), default="")
    difficulty: str = Field(index=True, nullable=False)
    solution: str = Field(sa_column=Column(Text), default="")
    constraints: str = Field(sa_column=Column(Text), default="")
    topic: str = Field(index=True, nullable=False)
    lang: str = Field(index=True, nullable=False)

    examples: List[Example] = Relationship(back_populates="problem")
