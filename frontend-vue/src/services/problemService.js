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
