<template>
  <div
    class="border-4 border-black rounded-lg p-6 bg-white shadow-[6px_6px_0px_0px_black] cursor-pointer hover:shadow-[10px_10px_0px_0px_black] transition-shadow"
    @click="$emit('select', { problemId: problem.id, studentId: student.id })"
    role="button"
    tabindex="0"
    @keyup.enter="$emit('select', { problemId: problem.id, studentId: student.id })"
  >
    <h2 class="font-bold text-2xl mb-2">{{ problem.title }}</h2>

    <div class="flex gap-2 mb-3">
      <NeoTab :text="getDifficultyText(problem.difficulty)" :bg="getDifficultyColor(problem.difficulty)" icon="trending_up" small />
      <NeoTab :text="problem.topic" bg="bg-[#E6E6FA]" icon="category" small />
      <NeoTab :text="problem.lang" bg="bg-[#FFD6A5]" icon="code" small />
      <NeoTab
        :text="statusText(problem.status)"
        :bg="statusColor(problem.status)"
        icon="info"
        small
      />
    </div>

    <p class="text-gray-700 text-sm mb-3 line-clamp-3">{{ problem.description }}</p>

    <div class="mb-3">
      <h4 class="font-semibold mb-1">Restricciones:</h4>
      <p class="text-gray-600 text-xs line-clamp-2">{{ problem.constraints }}</p>
    </div>

    <div class="border-t border-black pt-3 flex justify-between items-center text-sm text-gray-700 font-medium">
      <div>
        <span class="font-bold">Estudiante:</span> {{ student.name }}
      </div>
      <div>
        <span class="font-bold">Estado:</span> 
        <span :class="statusTextClass(problem.status)">{{ statusText(problem.status) }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import NeoTab from './NeoTab.vue';

const props = defineProps({
  problem: {
    type: Object,
    required: true,
  },
  student: {
    type: Object,
    required: true,
  },
});

const getDifficultyColor = (difficulty) => {
  switch (difficulty) {
    case 'facil': return 'bg-[#96FEAD]';
    case 'medio': return 'bg-[#FFD6A5]';
    case 'dificil': return 'bg-[#FFADAD]';
    default: return 'bg-gray-300';
  }
};

const getDifficultyText = (difficulty) => {
  switch (difficulty) {
    case 'facil': return 'Fácil';
    case 'medio': return 'Medio';
    case 'dificil': return 'Difícil';
    default: return 'Desconocido';
  }
};

const statusColor = (status) => {
  switch (status) {
    case 'pending': return 'bg-yellow-300';
    case 'in_revision': return 'bg-blue-300';
    case 'completed': return 'bg-green-300';
    default: return 'bg-gray-300';
  }
};

const statusText = (status) => {
  switch (status) {
    case 'pending': return 'Pendiente';
    case 'in_revision': return 'En revisión';
    case 'completed': return 'Aprobado';
    default: return 'Desconocido';
  }
};

const statusTextClass = (status) => {
  switch (status) {
    case 'pending': return 'text-yellow-700';
    case 'in_revision': return 'text-blue-700';
    case 'completed': return 'text-green-700';
    default: return 'text-gray-700';
  }
};
</script>
