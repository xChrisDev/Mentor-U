import axios from "axios";

export const getAllStudent = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/students/all");
    return response.data;
  } catch (error) {
    return { message: "Error al tratar de obtener los mentores" };
  }
};

export const getStudentByID = async (id) => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/students/get/${id}`
    );
    return response.data;
  } catch (error) {
    return { message: "Error al tratar de obtener el estudiante" };
  }
};

export const postStudent = async (data) => {
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/api/students/create",
      data,
      { "Content-Type": "multipart/form-data" }
    );
    return response.data;
  } catch (error) {
    return { message: "Error inesperado al tratar agregar estudiante" };
  }
};

export const putStudent = async (id, data) => {
  try {
    const response = await axios.put(
      `http://127.0.0.1:8000/api/students/update/${id}`,
      data,
      { "Content-Type": "multipart/form-data" }
    );
    return response.data;
  } catch (error) {
    return { message: "Error inesperado al tratar de editar estudiante" };
  }
};

export const deleteStudent = async (id) => {
  try {
    const response = await axios.delete(
      `http://127.0.0.1:8000/api/students/delete/${id}`
    );
    return response.data;
  } catch (error) {
    return { message: "Error inesperado al tratar de eliminar estudiante" };
  }
};
