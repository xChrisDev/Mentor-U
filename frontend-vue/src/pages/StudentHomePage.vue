<script setup>
import { onMounted } from 'vue';
import NeoButton from '../components/NeoButton.vue';
import { useAuth } from '../composables/useAuth';
import { useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';

const { clearUser, fetchUser, logout } = useAuth()
const toast = useToast()
const router = useRouter()
const mentor = ref(null)
defineProps({
  id: String
})

const fetchLogout = async () => {
  const res = await logout()
  toast.success(res.data.message, {
    toastClassName: "my-custom-toast-class",
  });
  router.push("/login")
}

onMounted(async () => {
  clearUser()
  const res = await fetchUser();
  mentor.value = res.data
  console.log(mentor.value)
})
</script>

<template>
  <div class="flex justify-center items-center" data-aos="zoom-in" data-aos-delay="100">
    <h1 class="font-ppgosha text-2xl">StudentHomePage</h1>
    <NeoButton text="Salir" icon="logout" bg="#96FEAD" class="mt-4 justify-center" @click="fetchLogout" />
  </div>
</template>
