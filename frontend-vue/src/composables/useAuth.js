import { ref } from 'vue'

const user = ref(null)
const role = ref(null)

export function useAuth() {
  const setUserData = (userData) => {
    user.value = userData.data
    role.value = userData.role
  }

  return { user, role, setUserData }
}
