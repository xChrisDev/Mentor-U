<script setup>
import NeoButton from '../NeoButton.vue';

const props = defineProps({
  mentoria: Object
});

const emit = defineEmits(['click', 'enroll']);
</script>

<template>
  <div class="border-2 border-black rounded-xl overflow-hidden bg-white flex flex-col">
    <!-- Imagen -->
    <img :src="mentoria.image || '/default-course.jpg'" alt="Imagen de mentoría"
      class="w-full h-40 object-cover border-b-2 border-black" />

    <!-- Contenido -->
    <div class="p-3 flex flex-col justify-between flex-1 gap-2">

      <!-- Info principal -->
      <div @click="emit('click')">
        <h4 class="font-bold text-lg mb-1">{{ mentoria.title }}</h4>
        <p class="text-sm text-gray-700 line-clamp-2">{{ mentoria.description }}</p>
      </div>

      <!-- Mentor + Estadísticas -->
      <div class="flex justify-between items-center text-xs">
        <!-- Mentor -->
        <div class="flex items-center gap-2">
          <img :src="mentoria.mentor?.profile_picture || '/default-avatar.png'" alt="Mentor"
            class="w-8 h-8 rounded-full border border-black object-cover" />
          <span class="text-sm">{{ mentoria.mentor?.name }} {{ mentoria.mentor?.surname }}</span>
        </div>

        <!-- Estadísticas -->
        <div class="flex gap-2">
          <span class="px-2 py-0.5 bg-[#F1E9FF] border border-black rounded-full flex items-center gap-1">
            <span class="material-symbols-rounded text-sm">schedule</span>
            {{ mentoria.duration }}h
          </span>
          <span class="px-2 py-0.5 bg-[#FFF6D1] border border-black rounded-full flex items-center gap-1">
            <span class="material-symbols-rounded text-sm">group</span>
            {{ mentoria.max_students }}
          </span>
        </div>
      </div>

      <!-- Pie -->
      <div class="flex justify-between items-center mt-1">
        <!-- Precio -->
        <div class="text-sm font-medium text-right">
          <span class="line-through text-gray-600">${{ mentoria.price.toFixed(2) }}</span>
          <span class="ml-1 text-green-500 font-bold">Gratis</span>
        </div>

        <!-- Botón -->
        <div v-if="!mentoria.is_enrolled">
          <NeoButton text="Inscribirse" icon="add_circle" bg="#96FEAD" @click="emit('enroll')" />
        </div>
        <div v-else class="border-2 border-black rounded-lg px-2 py-1">
          Ya inscrito
        </div>
      </div>
    </div>
  </div>
</template>

