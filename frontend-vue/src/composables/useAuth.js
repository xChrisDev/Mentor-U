import { ref } from "vue";
import axios from "axios";

axios.defaults.withCredentials = true;

export const user = ref(null);
export const userData = ref(null);
export const isLogged = ref(false);

export function useAuth() {
  const setUserData = (data) => {
    user.value = data;
    userData.value = data;
    isLogged.value = true;
  };

  const clearUserData = () => {
    user.value = null;
    userData.value = null;
    isLogged.value = false;
  };

  const clearUser = () => {
    user.value = null;
  };

  const login = async (data) => {
    try {
      const res = await axios.post(
        "http://localhost:8000/api/users/login",
        data
      );
      return res;
    } catch (error) {
      console.error("Login fallido", error);
      clearUserData();
    }
  };

  const fetchUser = async () => {
    try {
      const res = await axios.get("http://localhost:8000/api/users/me");
      setUserData(res.data);
      return res.data;
    } catch (error) {
      console.warn("No hay sesión activa");
      clearUserData();
    }
  };

  const logout = async () => {
    try {
      const res = await axios.post("http://localhost:8000/api/users/logout");
      return res;
    } catch (error) {
      console.warn("Error al cerrar sesión");
    } finally {
      clearUserData();
    }
  };

  return {
    user,
    userData,
    isLogged,
    login,
    logout,
    fetchUser,
    clearUser
  };
}
