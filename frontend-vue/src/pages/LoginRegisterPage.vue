<script setup>
import { onMounted, ref } from 'vue';
import NeoContainer from '../components/NeoContainer.vue';
import LoginForm from '../components/session-page/LoginForm.vue';
import SignUpForm from '../components/session-page/SignUpForm.vue';

const blobColors = ['#96FEAD', '#A0C4FF', '#FFADAD', '#FFD6A5'];
const blobs = ref([]);
const isLogin = ref(true);



onMounted(() => {
    blobs.value = Array.from({ length: 15 }).map(() => ({
        top: `${Math.random() * 100}%`,
        left: `${Math.random() * 100}%`,
        size: `${40 + Math.random() * 80}px`,
        duration: `${6 + Math.random() * 6}s`,
        delay: `${Math.random() * 4}s`,
        color: blobColors[Math.floor(Math.random() * blobColors.length)],
    }));
});

</script>

<template>
    <div class="fixed inset-0 z-50 flex items-center justify-center" data-aos="zoom-in" data-aos-delay="100">
  <div class="w-full lg:w-1/2 p-4">
    <NeoContainer bg="bg-white" class="w-full max-w-md p-8 flex flex-col gap-6 mx-auto">
      <h2 class="text-3xl font-ppgosha font-bold mb-2">
        {{ isLogin ? 'Iniciar Sesión' : 'Registrarse' }}
      </h2>

      <div v-if="isLogin" :key="isLogin">
        <LoginForm />
      </div>
      <div v-else>
        <SignUpForm />
      </div>

      <p class="text-sm text-center">
        {{ isLogin ? '¿No tienes cuenta?' : '¿Ya tienes cuenta?' }}
        <button
          class="text-purple-600 font-semibold ml-1 cursor-pointer hover:underline"
          @click="isLogin = !isLogin"
        >
          {{ isLogin ? 'Regístrate' : 'Inicia sesión' }}
        </button>
      </p>
    </NeoContainer>
  </div>
</div>


    <div class="fixed inset-0 -z-9 overflow-hidden pointer-events-none">
        <div v-for="(blob, index) in blobs" :key="index" class="absolute blob" :style="{
            top: blob.top,
            left: blob.left,
            width: blob.size,
            height: blob.size,
            backgroundColor: blob.color,
            animationDuration: blob.duration,
            animationDelay: blob.delay
        }"></div>
    </div>


</template>
