from fastapi import APIRouter, HTTPException
from schemas.problem_scheme import ProblemCreate, ProblemWithExamples
from typing import List 
from services.problem_services import (
    create_problem,
    get_problem_by_id,
    get_problems_by_lang,
    get_problem_by_mentorie_id,
    update_problem,
    remove_problem
)

router = APIRouter(prefix="/api/problems", tags=["Problems"])


@router.post("/create")
def generate_problem(problem: ProblemCreate):
    new_problem = create_problem(problem.topic, problem.lang, problem.level, problem.id_mentor, problem.id_mentorie)
    if not new_problem:
        raise HTTPException(status_code=400, detail="Error al crear el problema")
    return {"message": "Problema creado correctamente", "problem": new_problem}

@router.put("/update/{problem_id}")
def put_problem(problem_id: int, problem: ProblemWithExamples):
    response = update_problem(
        problem_id,
        problem.title,
        problem.description,
        problem.difficulty,
        problem.constraints,
        problem.solution,
        problem.topic,
        problem.lang,
        problem.examples,
        problem.id_mentor,
        problem.id_mentorie
    )
    if not response:
        raise HTTPException(status_code=404, detail="Problema no encontrado")
    return response

@router.delete("/delete/{problem_id}")
def delete_problem(problem_id: int):
    response = remove_problem(problem_id)
    if not response:
        raise HTTPException(status_code=404, detail="Problema no encontrado")
    return {"message": "Problema eliminado correctamente"}

@router.get("/get/{problem_id}", response_model=ProblemWithExamples)
def get_problem(problem_id: int):
    problem = get_problem_by_id(problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problema no encontrado")
    return problem

@router.get("/get/mentor/{mentorie_id}")
def get_problem(mentorie_id: int):
    problems = get_problem_by_mentorie_id(mentorie_id)
    if not problems:
        raise HTTPException(status_code=404, detail="Problema no encontrado")
    return problems

@router.get("/get/lang/{lang}", response_model=List[ProblemWithExamples])
def get_problems_by_language(lang: str):
    problems = get_problems_by_lang(lang)
    if not problems:
        raise HTTPException(status_code=404, detail="Problemas no encontrados")
    return problems