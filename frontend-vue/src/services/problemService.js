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
      `http://127.0.0.1:8000/api/problems/get/mentor/${id}`,
    );
    return response.data;
  } catch (error) {
    console.log(error);
    return { message: "Error inesperado al generar problema con IA" };
  }
};
