import os
import requests
import json
import re
from sqlmodel import Session, select
from core.database import engine
from models.problem_model import Problem, Example
from dotenv import load_dotenv
from sqlalchemy.orm import selectinload


def create_problem(topic: str, lang: str, level: str, id_mentor: int, id_mentorie: int):
    with Session(engine) as session:
        existing_problem = session.exec(
            select(Problem).where(
                Problem.topic == topic,
                Problem.difficulty == level,
                Problem.lang == lang,
            )
        ).first()
        if existing_problem:
            return existing_problem
        else:
            message = {
                "message": f"""
            Actúa como un profesor experto en programación. Genera un ejercicio sobre {topic} con calidad LeetCode (nivel {level}).

            REQUISITOS ESTRICTOS:
            1. Devuelve SOLO un JSON válido (sin texto adicional)
            2. Usa comillas dobles (") para strings (no comillas simples)
            3. Escapa correctamente caracteres especiales en strings (\\", \\n, etc.)
            4. Formato consistente para arrays y objetos
            5. La solución debe estar en {lang} con el formato exacto:
               ```{lang}\n[code]\n```

            ESTRUCTURA EXACTA REQUERIDA:
            {{
                "title": "string",
                "description": "string",
                "difficulty": "facil|medio|dificil",
                "examples": [
                    {{
                        "input": "string",
                        "output": "string",
                        "explanation": "string"
                    }}
                ],
                "constraints": "string",
                "solution": "string (formato ```lang\\n[code]\\n```)"
            }}

            Pautas específicas:
            - En 'input/output' usa representaciones literales de código: "[1,2,3]" en lugar de [1,2,3]
            - 'difficulty' debe coincidir con {level} (facil/medio/dificil)
            - La solución debe ser ejecutable y bien comentada
            - Explicaciones claras y completas
            """
            }
            load_dotenv()
            URL = os.getenv("IA_URL")
            response = requests.post(URL, json=message)
            try:
                if response.status_code == 200:
                    data = response.json()
                    reply_raw = data.get("reply", "").strip()

                    if not reply_raw:
                        return None

                    match = re.search(
                        r"```(?:json)?\s*(\{.*?\})\s*```", reply_raw, re.DOTALL
                    )
                    json_text = match.group(1) if match else reply_raw

                    reply_json = json.loads(json_text)

                    examples = reply_json.get("examples")
                    problem = Problem(
                        title=reply_json.get("title"),
                        description=reply_json.get("description"),
                        difficulty=reply_json.get("difficulty"),
                        constraints=reply_json.get("constraints"),
                        solution=reply_json.get("solution"),
                        topic=topic,
                        lang=lang,
                        id_mentor=id_mentor,
                        id_mentorie=id_mentorie
                    )
                    session.add(problem)
                    session.commit()
                    session.refresh(problem)

                    for example in examples:
                        example_obj = Example(
                            input=example.get("input"),
                            output=example.get("output"),
                            explanation=example.get("explanation"),
                            problem_id=problem.id,
                        )
                        session.add(example_obj)

                    session.commit()
                    session.refresh(problem)

                    return problem
                else:
                    return None
            except Exception as e:
                print("Error al crear el problema:", str(e))
                return None


def get_problem_by_id(problem_id: int):
    with Session(engine) as session:
        statement = (
            select(Problem)
            .where(Problem.id == problem_id)
            .options(selectinload(Problem.examples))
        )
        problem = session.exec(statement).first()
        if not problem:
            return None
        return problem


def get_problem_by_mentorie_id(mentorie_id: int):
    with Session(engine) as session:
        statement = (
            select(Problem)
            .where(Problem.id_mentorie == mentorie_id)
            .options(selectinload(Problem.examples))
        )
        problems = session.exec(statement).all()
        if not problems:
            return None
        return problems


def get_problems_by_lang(lang: str):
    with Session(engine) as session:
        statement = (
            select(Problem)
            .where(Problem.lang == lang)
            .options(selectinload(Problem.examples))
        )
        problems = session.exec(statement).all()
        if not problems:
            return None
        return problems


def update_problem(
    problem_id: int,
    title: str,
    description: str,
    difficulty: str,
    constraints: str,
    solution: str,
    topic: str,
    lang: str,
    examples: list,
    id_mentor : int,
    id_mentorie: int
):
    with Session(engine) as session:
        statement = select(Problem).where(Problem.id == problem_id)
        problem = session.exec(statement).first()
        if not problem:
            return None

        problem.title = title
        problem.description = description
        problem.difficulty = difficulty
        problem.constraints = constraints
        problem.solution = solution
        problem.topic = topic
        problem.lang = lang
        problem.id_mentor = id_mentor
        problem.id_mentorie = id_mentorie

        for ex in problem.examples:
            session.delete(ex)
        session.commit()

        for example in examples:
            example_data = example if isinstance(example, dict) else example.dict()
            new_example = Example(
                input=example_data["input"],
                output=example_data["output"],
                explanation=example_data["explanation"],
                problem_id=problem.id,
            )
            session.add(new_example)

        session.commit()
        session.refresh(problem)

        return {"message": "Problema actualizado correctamente", "problem": problem}


def remove_problem(problem_id: int):
    with Session(engine) as session:
        statement = select(Problem).where(Problem.id == problem_id)
        problem = session.exec(statement).first()
        if not problem:
            return {"message": "Problema no encontrado"}

        for ex in problem.examples:
            session.delete(ex)

        session.delete(problem)
        session.commit()
        return {"message": "Problema eliminado correctamente"}
