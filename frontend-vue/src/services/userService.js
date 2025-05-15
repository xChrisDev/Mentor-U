import axios from "axios";

const registerUser = async (data) => {
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

const loginUser = async () => {
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/api/users/login",
      data
    );
    return response.data;
  } catch (error) {
    return { message: "Error al iniciar sesión" };
  }
};

const deleteAccount = async (id) => {
  try {
    const response = await axios.delete(
      `http://127.0.0.1:8000/api/users/delete/${id}`
    );
    return response.data;
  } catch (error) {
    return { message: "Error al tratar de eliminar la cuenta" };
  }
};

const updateUser = async (id, data) => {
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
