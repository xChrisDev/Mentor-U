import axios from "axios";

export const registerUser = async (data) => {
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/api/users/register",
      data
    );
    return response.data;
  } catch (error) {
    return { message: "Error inesperado al registrarse" };
  }
};

export const deleteAccount = async (id) => {
  try {
    const response = await axios.delete(
      `http://127.0.0.1:8000/api/users/delete/${id}`
    );
    return response.data;
  } catch (error) {
    return { message: "Error al tratar de eliminar la cuenta" };
  }
};

export const updateUser = async (id, data) => {
  try {
    const response = await axios.put(
      `http://127.0.0.1:8000/api/users/update/${id}`,
      data
    );
    return response.data;
  } catch (error) {
    return { message: "Error al tratar de actualizar su información" };
  }
};

export const getUserData = async (username) => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/users/get_user_data/${username}`
    );
    return response.data;
  } catch (error) {
    return { message: "Error al tratar de obtener la información" };
  }
};

export const getUser = async (id) => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/users/get_user_by_id/${id}`
    );
    return response.data;
  } catch (error) {
    return { message: "Error al tratar de obtener la información" };
  }
};
