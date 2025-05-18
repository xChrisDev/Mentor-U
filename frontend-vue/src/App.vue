<script setup>
import { onMounted } from 'vue';
import { useAuth } from './composables/useAuth';

const auth = useAuth()

onMounted(() => {
  auth.fetchUser()
})
</script>

<template>
  <div class="relative min-h-screen w-full pb-20">
    <div class="absolute inset-0 -z-10 h-full w-full
             bg-white
             bg-[radial-gradient(#edd_2px,transparent_1px)]
             [background-size:24px_24px]">
    </div>

    <main class="container mx-auto w-[75%] pt-8">
      <RouterView />
    </main>
  </div>
</template>
