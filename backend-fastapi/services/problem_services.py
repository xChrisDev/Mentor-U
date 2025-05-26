import os
import requests
import json
import re
from sqlmodel import Session, select
from core.database import engine
from models.problem_model import Problem, Example
from dotenv import load_dotenv
from sqlalchemy.orm import selectinload
from models.student_problems_link import StudentProblemLink
from models.mentory_students_link import MentoryStudentLink


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

def get_problems_by_mentory_and_student(mentory_id: int, student_id: int):
    with Session(engine) as session:
        # Obtener todos los problemas de esa mentoría
        problems = session.exec(
            select(Problem).where(Problem.id_mentorie == mentory_id)
        ).all()

        results = []

        for problem in problems:
            # Verificar si ya existe el vínculo
            link = session.exec(
                select(StudentProblemLink).where(
                    (StudentProblemLink.problem_id == problem.id) &
                    (StudentProblemLink.student_id == student_id)
                )
            ).first()

            # Si no existe, crearlo como pendiente
            if not link:
                link = StudentProblemLink(
                    problem_id=problem.id,
                    student_id=student_id,
                    status="pendiente"
                )
                session.add(link)
                session.commit()
                session.refresh(link)

            # Obtener los ejemplos del problema
            examples = session.exec(
                select(Example).where(Example.problem_id == problem.id)
            ).all()

            results.append({
                "id": problem.id,
                "title": problem.title,
                "description": problem.description,
                "difficulty": problem.difficulty,
                "solution": problem.solution,
                "constraints": problem.constraints,
                "topic": problem.topic,
                "lang": problem.lang,
                "id_mentor": problem.id_mentor,
                "id_mentorie": problem.id_mentorie,
                "examples": [
                    {
                        "id": e.id,
                        "input": e.input,
                        "output": e.output,
                        "explanation": e.explanation,
                        "problem_id": e.problem_id
                    } for e in examples
                ],
                "status": link.status
            })

        return results

        
def update_mentory_progress(student_id: int, mentory_id: int):
    with Session(engine) as session:
        # Obtener todos los problemas de esa mentoría
        all_problems = session.exec(
            select(Problem).where(Problem.id_mentorie == mentory_id)
        ).all()

        total_problems = len(all_problems)
        if total_problems == 0:
            return {"message": "No hay problemas registrados para esta mentoría."}

        # Obtener todos los problemas que el estudiante ha completado en esta mentoría
        completed_count = 0
        for problem in all_problems:
            link = session.exec(
                select(StudentProblemLink).where(
                    (StudentProblemLink.problem_id == problem.id) &
                    (StudentProblemLink.student_id == student_id) &
                    (StudentProblemLink.status == "completado")
                )
            ).first()

            if link:
                completed_count += 1

        # Calcular el progreso (entero entre 0 y 100)
        progress = int((completed_count / total_problems) * 100)

        # Buscar el enlace entre estudiante y mentoría
        mentory_link = session.exec(
            select(MentoryStudentLink).where(
                (MentoryStudentLink.student_id == student_id) &
                (MentoryStudentLink.mentory_id == mentory_id)
            )
        ).first()

        if not mentory_link:
            mentory_link = MentoryStudentLink(
                student_id=student_id,
                mentory_id=mentory_id,
                progress=progress,
                status=(
                    "not_started" if progress == 0 else
                    "completed" if progress == 100 else
                    "in_progress"
                )
            )
            session.add(mentory_link)
        else:
            mentory_link.progress = progress
            mentory_link.status = (
                "not_started" if progress == 0 else
                "completed" if progress == 100 else
                "in_progress"
            )

        session.commit()
        session.refresh(mentory_link)

        return {
            "mentory_id": mentory_id,
            "student_id": student_id,
            "progress": progress,
            "status": mentory_link.status
        }
        

def update_problem_status(student_id: int, problem_id: int, status: str):
    with Session(engine) as session:
        # Obtener o crear el vínculo problema-estudiante
        link = session.exec(
            select(StudentProblemLink).where(
                (StudentProblemLink.student_id == student_id) &
                (StudentProblemLink.problem_id == problem_id)
            )
        ).first()

        if not link:
            link = StudentProblemLink(
                student_id=student_id,
                problem_id=problem_id,
                status=status
            )
            session.add(link)
        else:
            link.status = status

        session.commit()

        # Obtener el problema para saber a qué mentoría pertenece
        problem = session.get(Problem, problem_id)
        if not problem:
            return {"message": "Problema no encontrado."}

        # Llamar al servicio que actualiza el progreso de la mentoría
        updated_progress = update_mentory_progress(student_id, problem.id_mentorie)

        return {
            "message": "Estado actualizado correctamente.",
            "problem_id": problem_id,
            "new_status": status,
            "mentory_progress": updated_progress
        }


def get_problem_by_mentorie_id(mentorie_id: int):
    with Session(engine) as session:
        problems = session.exec(
            select(Problem).where(Problem.id_mentorie == mentorie_id)
        ).all()

        if not problems:
            return None

        result = []
        for problem in problems:
            examples = session.exec(
                select(Example).where(Example.problem_id == problem.id)
            ).all()

            result.append({
                "id": problem.id,
                "title": problem.title,
                "description": problem.description,
                "difficulty": problem.difficulty,
                "solution": problem.solution,
                "constraints": problem.constraints,
                "topic": problem.topic,
                "lang": problem.lang,
                "id_mentor": problem.id_mentor,
                "id_mentorie": problem.id_mentorie,
                "examples": [
                    {
                        "id": e.id,
                        "input": e.input,
                        "output": e.output,
                        "explanation": e.explanation,
                        "problem_id": e.problem_id
                    }
                    for e in examples
                ]
            })

        return result

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
