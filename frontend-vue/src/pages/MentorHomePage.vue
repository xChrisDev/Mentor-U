<script setup>
import { onMounted } from 'vue';
import NeoButton from '../components/NeoButton.vue';
import { useAuth } from '../composables/useAuth';

const { clearUser } = useAuth()
defineProps({
  id: String
})

const fetchLogout = () => {
  console.log("salir")
}

onMounted(() => {
  clearUser()
})
</script>

<template>
  <div class="flex justify-center items-center" data-aos="zoom-in" data-aos-delay="100">
    <h1 class="font-ppgosha text-2xl">MentorHomePage</h1>
    <NeoButton text="Salir" icon="logout" bg="#96FEAD" class="mt-4 justify-center" @click="fetchLogout" />
  </div>
</template>
