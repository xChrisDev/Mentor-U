import axios from "axios";

export const postProblem = async (data) => {
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/api/problems/create",
      data
    );
    return response.data;
  } catch (error) {
    console.log(error);
    return { message: "Error inesperado al generar problema con IA" };
  }
};

export const getProblemsByMentorID = async (id) => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/problems/get/mentor/${id}`
    );
    return response.data;
  } catch (error) {
    console.log(error);
    return { message: "Error inesperado al obtener problemas" };
  }
};

export const getSolutionsByMentorID = async (id) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/api/problems/student-solutions/?mentor_id=${id}`
    );
    return response.data;
  } catch (error) {
    console.log(error);
    return { message: "Error inesperado al obtener problemas" };
  }
};

export const getSolutionByID = async (id) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/api/problems/student-solutions/get/?solution_id=${id}`
    );
    return response.data;
  } catch (error) {
    console.log(error);
    return { message: "Error inesperado al obtener problemas" };
  }
};

export const getSolutionByCompositeKey = async (problemId, studentId, mentorieId) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/api/problems/student-solutions/find/`,
      {
        params: {
          problem_id: problemId,
          student_id: studentId,
          mentorie_id: mentorieId,
        },
      }
    );
    return response.data;
  } catch (error) {
    console.log(error);
    return { message: "Error inesperado al obtener la solución" };
  }
};


export const getProblemByID = async (id_problem, id_student) => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/problems/get/${id_problem}/${id_student}`
    );
    return response.data;
  } catch (error) {
    console.log(error);
    return { message: "Error inesperado al obtener problemas" };
  }
};

export const updateProgress = async (id, data) => {
  try {
    const response = await axios.put(
      `http://127.0.0.1:8000/api/problems/${id}/progress`,
      data
    );
    return response.data;
  } catch (error) {
    console.log(error);
    return { message: "Error inesperado al actualizar progreso de problemas" };
  }
};

export const updateProblemStatus = async (id, data) => {
  try {
    const response = await axios.put(
      `http://127.0.0.1:8000/api/problems/${id}/status`,
      data
    );
    return response.data;
  } catch (error) {
    console.log(error);
    return { message: "Error inesperado al actualizar status de problema" };
  }
};

export const postStudentSolution = async (data) => {
  try {
    const response = await axios.post(
      `http://127.0.0.1:8000/api/problems/student-solutions`,
      data
    );
    return response.data;
  } catch (error) {
    console.log(error);
    return { message: "Error inesperado al agregar solucion" };
  }
};

export const updateStudentSolution = async (solution_id, data) => {
  try {
    const response = await axios.put(
      `http://127.0.0.1:8000/api/problems/student-solutions/${solution_id}`,
      data
    );
    return response.data;
  } catch (error) {
    console.log(error);
    return { message: "Error inesperado al actualizar solucion" };
  }
};

export async function getMentoryProblemsByStudent(mentoryId, studentId) {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/problems/mentory/${mentoryId}/student/${studentId}/problems`
    );
    return response.data;
  } catch (error) {
    console.error("Error al obtener los problemas de la mentoría:", error);
    return [];
  }
}

export async function testCode(data) {
  try {
    const response = await axios.post(
      `http://127.0.0.1:8000/api/problems/test-code`,
      data
    );
    return response.data;
  } catch (error) {
    console.error("Error al obtener los problemas de la mentoría:", error);
    return [];
  }
}
