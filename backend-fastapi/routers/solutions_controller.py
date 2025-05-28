from fastapi import APIRouter, HTTPException, Depends, status
from sqlmodel import Session, select
from core.database import engine
from typing import List, Optional
from datetime import datetime, timezone

from models.student_solution import (
    StudentSolution, 
    StudentSolutionCreate, 
    StudentSolutionUpdate,
    StudentSolutionWithDetails
)
from models.problem_model import Problem
from models.student_model import Student
from models.mentor_model import Mentory

router = APIRouter(prefix="/student-solutions", tags=["Student Solutions"])


@router.post("/", response_model=StudentSolution, status_code=status.HTTP_201_CREATED)
async def create_student_solution(
    solution_data: StudentSolutionCreate
):
    """
    Crear una nueva solución de estudiante
    """
    with Session(engine) as session:
        # Verificar que existan el problema, estudiante y mentoría
        problem = session.get(Problem, solution_data.problem_id)
        if not problem:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Problem not found"
            )
        
        student = session.get(Student, solution_data.student_id)
        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )
        
        mentorie = session.get(Mentory, solution_data.mentorie_id)
        if not mentorie:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Mentorie not found"
            )
        
        # Verificar si ya existe una solución para este problema/estudiante/mentoría
        existing_solution = session.exec(
            select(StudentSolution).where(
                StudentSolution.problem_id == solution_data.problem_id,
                StudentSolution.student_id == solution_data.student_id,
                StudentSolution.mentorie_id == solution_data.mentorie_id
            )
        ).first()
        
        if existing_solution:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Solution already exists for this problem/student/mentorie combination"
            )
        
        # Crear la nueva solución
        new_solution = StudentSolution(**solution_data.model_dump())
        session.add(new_solution)
        session.commit()
        session.refresh(new_solution)
        
        return new_solution


@router.get("/{solution_id}", response_model=StudentSolutionWithDetails)
async def get_student_solution_with_details(
    solution_id: int
):
    """
    Obtener información completa de una solución (con detalles del problema, estudiante y mentoría)
    """
    with Session(engine) as session:
        # Query con joins para obtener toda la información
        query = select(
            StudentSolution,
            Problem.title.label("problem_title"),
            Problem.description.label("problem_description"),
            Problem.difficulty.label("problem_difficulty"),
            Problem.topic.label("problem_topic"),
            Student.name.label("student_name"),
            Student.surname.label("student_surname"),
            Mentory.title.label("mentorie_title"),
            Mentory.description.label("mentorie_description")
        ).join(
            Problem, StudentSolution.problem_id == Problem.id
        ).join(
            Student, StudentSolution.student_id == Student.id
        ).join(
            Mentory, StudentSolution.mentorie_id == Mentory.id
        ).where(
            StudentSolution.id == solution_id
        )
        
        result = session.exec(query).first()
        
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student solution not found"
            )
        
        solution, problem_title, problem_description, problem_difficulty, problem_topic, \
        student_name, student_surname, mentorie_title, mentorie_description = result
        
        return StudentSolutionWithDetails(
            id=solution.id,
            problem_id=solution.problem_id,
            student_id=solution.student_id,
            mentorie_id=solution.mentorie_id,
            code=solution.code,
            comments=solution.comments,
            result=solution.result,
            created_at=solution.created_at,
            updated_at=solution.updated_at,
            problem_title=problem_title,
            problem_description=problem_description,
            problem_difficulty=problem_difficulty,
            problem_topic=problem_topic,
            student_name=student_name,
            student_surname=student_surname,
            mentorie_title=mentorie_title,
            mentorie_description=mentorie_description
        )


@router.get("/", response_model=List[StudentSolutionWithDetails])
async def get_all_student_solutions_with_details(
    student_id: Optional[int] = None,
    problem_id: Optional[int] = None,
    mentorie_id: Optional[int] = None,
    result: Optional[str] = None
):
    with Session(engine) as session:
        """
        Obtener todas las soluciones con filtros opcionales
        """
        query = select(
            StudentSolution,
            Problem.title.label("problem_title"),
            Problem.description.label("problem_description"),
            Problem.difficulty.label("problem_difficulty"),
            Problem.topic.label("problem_topic"),
            Student.name.label("student_name"),
            Student.surname.label("student_surname"),
            Mentory.title.label("mentorie_title"),
            Mentory.description.label("mentorie_description")
        ).join(
            Problem, StudentSolution.problem_id == Problem.id
        ).join(
            Student, StudentSolution.student_id == Student.id
        ).join(
            Mentory, StudentSolution.mentorie_id == Mentory.id
        )
        
        # Aplicar filtros
        if student_id:
            query = query.where(StudentSolution.student_id == student_id)
        if problem_id:
            query = query.where(StudentSolution.problem_id == problem_id)
        if mentorie_id:
            query = query.where(StudentSolution.mentorie_id == mentorie_id)
        if result:
            query = query.where(StudentSolution.result == result)
        
        results = session.exec(query).all()
        
        solutions_with_details = []
        for result in results:
            solution, problem_title, problem_description, problem_difficulty, problem_topic, \
            student_name, student_surname, mentorie_title, mentorie_description = result
            
            solutions_with_details.append(StudentSolutionWithDetails(
                id=solution.id,
                problem_id=solution.problem_id,
                student_id=solution.student_id,
                mentorie_id=solution.mentorie_id,
                code=solution.code,
                comments=solution.comments,
                result=solution.result,
                created_at=solution.created_at,
                updated_at=solution.updated_at,
                problem_title=problem_title,
                problem_description=problem_description,
                problem_difficulty=problem_difficulty,
                problem_topic=problem_topic,
                student_name=student_name,
                student_surname=student_surname,
                mentorie_title=mentorie_title,
                mentorie_description=mentorie_description
            ))
        
        return solutions_with_details


@router.put("/{solution_id}", response_model=StudentSolution)
async def update_student_solution(
    solution_id: int,
    solution_update: StudentSolutionUpdate
):
    with Session(engine) as session:
        """
        Actualizar una solución existente
        """
        solution = session.get(StudentSolution, solution_id)
        if not solution:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student solution not found"
            )
        
        # Actualizar solo los campos proporcionados
        update_data = solution_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(solution, field, value)
        
        # Actualizar timestamp
        solution.updated_at = datetime.now(timezone.utc)
        
        session.add(solution)
        session.commit()
        session.refresh(solution)
        
        return solution


@router.delete("/{solution_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student_solution(
    solution_id: int
):
    with Session(engine) as session:
        """
        Eliminar una solución
        """
        solution = session.get(StudentSolution, solution_id)
        if not solution:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student solution not found"
            )
        
        session.delete(solution)
        session.commit()


@router.get("/student/{student_id}/mentorie/{mentorie_id}", response_model=List[StudentSolutionWithDetails])
async def get_student_solutions_by_mentorie(
    student_id: int,
    mentorie_id: int
):
    with Session(engine) as session:
        """
        Obtener todas las soluciones de un estudiante específico en una mentoría específica
        """
        query = select(
            StudentSolution,
            Problem.title.label("problem_title"),
            Problem.description.label("problem_description"),
            Problem.difficulty.label("problem_difficulty"),
            Problem.topic.label("problem_topic"),
            Student.name.label("student_name"),
            Student.surname.label("student_surname"),
            Mentory.title.label("mentorie_title"),
            Mentory.description.label("mentorie_description")
        ).join(
            Problem, StudentSolution.problem_id == Problem.id
        ).join(
            Student, StudentSolution.student_id == Student.id
        ).join(
            Mentory, StudentSolution.mentorie_id == Mentory.id
        ).where(
            StudentSolution.student_id == student_id,
            StudentSolution.mentorie_id == mentorie_id
        )
        
        results = session.exec(query).all()
        
        solutions_with_details = []
        for result in results:
            solution, problem_title, problem_description, problem_difficulty, problem_topic, \
            student_name, student_surname, mentorie_title, mentorie_description = result
            
            solutions_with_details.append(StudentSolutionWithDetails(
                id=solution.id,
                problem_id=solution.problem_id,
                student_id=solution.student_id,
                mentorie_id=solution.mentorie_id,
                code=solution.code,
                comments=solution.comments,
                result=solution.result,
                created_at=solution.created_at,
                updated_at=solution.updated_at,
                problem_title=problem_title,
                problem_description=problem_description,
                problem_difficulty=problem_difficulty,
                problem_topic=problem_topic,
                student_name=student_name,
                student_surname=student_surname,
                mentorie_title=mentorie_title,
                mentorie_description=mentorie_description
            ))
        
        return solutions_with_details