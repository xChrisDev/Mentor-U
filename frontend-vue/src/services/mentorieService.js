import axios from "axios";

export const getAllMentories = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/mentories/all");
    return response.data;
  } catch (error) {
    return { message: "Error al tratar obtener las mentorias" };
  }
};

export const getMentorieByID = async (id) => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/mentories/get/${id}`
    );
    return response.data;
  } catch (error) {
    return { message: "Error al tratar de obtener las mentorias" };
  }
};

export const getMentorieDetailByID = async (id) => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/mentories/get/mentorie/${id}`
    );
    return response.data;
  } catch (error) {
    return { message: "Error al tratar de obtener la mentoria" };
  }
};

export const postMentorie = async (data) => {
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/api/mentories/create",
      data,
      { "Content-Type": "multipart/form-data" }
    );
    return response.data;
  } catch (error) {
    return { message: "Error inesperado al tratar agregar mentoria" };
  }
};

export const putMentorie = async (id, data) => {
  try {
    const response = await axios.put(
      `http://127.0.0.1:8000/api/mentories/update/${id}`,
      data,
      { "Content-Type": "multipart/form-data" }
    );
    return response.data;
  } catch (error) {
    console.log(error)
    return { message: "Error inesperado al tratar de editar mentoria" };
  }
};

export const deleteMentorie = async (id) => {
  try {
    const response = await axios.delete(
      `http://127.0.0.1:8000/api/mentories/delete/${id}`
    );
    return response.data;
  } catch (error) {
    return { message: "Error inesperado al tratar de eliminar mentoria" };
  }
};
