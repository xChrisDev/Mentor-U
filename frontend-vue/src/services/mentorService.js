import axios from "axios";

export const getAllMentors = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/mentors/all");
    return response.data;
  } catch (error) {
    return { message: "Error al obtener los mentores" };
  }
};

export const getMentorByID = async (id) => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/mentors/get/${id}`
    );
    return response.data;
  } catch (error) {
    return { message: "Error al obtener mentor" };
  }
};

export const getTechsByID = async (id) => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/mentors/${id}/technologies`
    );
    return response.data;
  } catch (error) {
    return { message: "Error al tratar de obtener las tecnologias" };
  }
};

export const postMentor = async (data) => {
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/api/mentors/create",
      data,
      { "Content-Type": "multipart/form-data" }
    );
    return response.data;
  } catch (error) {
    console.log(error)
    return { message: "Error inesperado al tratar agregar mentor" };
  }
};

export const putMentor = async (id, data) => {
  try {
    const response = await axios.put(
      `http://127.0.0.1:8000/api/mentors/update/${id}`,
      data,
      { "Content-Type": "multipart/form-data" }
    );
    return response.data;
  } catch (error) {
    return { message: "Error inesperado al tratar de editar mentor" };
  }
};

export const deleteMentor = async (id) => {
  try {
    const response = await axios.delete(
      `http://127.0.0.1:8000/api/mentors/delete/${id}`
    );
    return response.data;
  } catch (error) {
    return { message: "Error inesperado al tratar de eliminar mentor" };
  }
};
