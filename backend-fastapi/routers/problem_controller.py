from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
import re
import requests
import os
import json
from schemas.problem_scheme import (
    ProblemCreate,
    ProblemWithExamples,
    ProblemProgress,
    ProblemStatusUpdate,
    PromptRequest,
)
from typing import List
from services.problem_services import (
    create_problem,
    get_problem_by_id,
    get_problems_by_lang,
    get_problem_by_mentorie_id,
    update_problem,
    remove_problem,
    get_problems_by_mentory_and_student,
    update_problem_status,
    update_mentory_progress,
)

router = APIRouter(prefix="/api/problems", tags=["Problems"])


@router.post("/create")
def generate_problem(problem: ProblemCreate):
    new_problem = create_problem(
        problem.topic,
        problem.lang,
        problem.level,
        problem.id_mentor,
        problem.id_mentorie,
    )
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
        problem.id_mentorie,
    )
    if not response:
        raise HTTPException(status_code=404, detail="Problema no encontrado")
    return response


@router.put("/{problem_id}/status")
def update_status(problem_id: int, problem: ProblemStatusUpdate):
    return update_problem_status(problem.student_id, problem_id, problem.status)


@router.put(
    "/{mentorie_id}/progress",
)
def update_progress(mentorie_id: int, problem: ProblemProgress):
    return update_mentory_progress(
        student_id=problem.student_id, mentory_id=mentorie_id
    )


@router.delete("/delete/{problem_id}")
def delete_problem(problem_id: int):
    response = remove_problem(problem_id)
    if not response:
        raise HTTPException(status_code=404, detail="Problema no encontrado")
    return {"message": "Problema eliminado correctamente"}


@router.get("/get/mentor/{mentorie_id}")
def get_problem_mentorie(mentorie_id: int):
    problems = get_problem_by_mentorie_id(mentorie_id)
    if problems:
        return problems


@router.get(
    "/get/{problem_id}/{student_id}",
)
def get_problem(problem_id: int, student_id: int):
    problem = get_problem_by_id(problem_id, student_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problema no encontrado")
    return problem


@router.get("/get/lang/{lang}", response_model=List[ProblemWithExamples])
def get_problems_by_language(lang: str):
    problems = get_problems_by_lang(lang)
    if not problems:
        raise HTTPException(status_code=404, detail="Problemas no encontrados")
    return problems


@router.get("/mentory/{mentory_id}/student/{student_id}/problems")
def get_mentory_problems(mentory_id: int, student_id: int):
    return get_problems_by_mentory_and_student(mentory_id, student_id)


@router.post("/test-code")
async def test_code_endpoint(request: PromptRequest):
    prompt = """
    Actúa como un evaluador automático de código para problemas de programación.

    RECIBIRÁS:
    - Un fragmento de código en lenguaje {lang}
    - Una lista de casos de prueba, con entradas y salidas esperadas

    REQUISITOS ESTRICTOS:
    1. Devuelve SOLO un JSON válido (sin texto adicional)
    2. Usa comillas dobles (") para strings (no comillas simples)
    3. Escapa correctamente caracteres especiales en strings (\\", \\n, etc.)
    4. Formato consistente para arrays y objetos
    5. No formatees como markdown, no uses ```{lang}``` en la respuesta final

    FORMATO EXACTO REQUERIDO EN LA RESPUESTA:
    {{
    "results": [
        {{
        "input": "string",
        "expected_output": "string",
        "actual_output": "string",
        "passed": true | false,
        "error": null | "mensaje de error"
        }}
    ]
    }}

    INSTRUCCIONES:
    - Ejecuta el código tal como está
    - Para cada entrada, evalúa el resultado y compáralo con la salida esperada
    - Si ocurre un error en ejecución, inclúyelo en el campo "error" y pon "actual_output" como null
    - Devuelve un objeto JSON con una lista de resultados por prueba
    - No expliques nada, no incluyas texto adicional

    DATOS DE ENTRADA:
    Lenguaje: {lang}
    Código:
    ```{lang}
    {code}
    Casos de prueba:
{examples}
""".format(
        lang=request.lang, code=request.code, examples=request.examples
    )

    message = {"message": prompt}

    load_dotenv()
    URL = os.getenv("IA_URL")
    response = requests.post(URL, json=message)

    try:
        if response.status_code == 200:
            data = response.json()
            reply_raw = data.get("reply", "").strip()

            if not reply_raw:
                return None
            match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", reply_raw, re.DOTALL)
            json_text = match.group(1) if match else reply_raw
            reply_json = json.loads(json_text)

            return {"success": True, "message": reply_json}
        else:
            return {
                "success": False,
                "message": f"Error en la solicitud a IA: código {response.status_code}",
            }
    except Exception as e:
        print("Error al procesar la respuesta:", str(e))
        return {"error": "Hubo un problema al procesar la respuesta de la IA"}
