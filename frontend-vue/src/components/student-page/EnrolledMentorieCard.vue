<script setup>
import NeoButton from '../NeoButton.vue';
import NeoTab from '../NeoTab.vue';

const props = defineProps({
  mentoria: Object
})

const emit = defineEmits(['click'])

const getProgressColor = (progress) => {
  if (progress >= 80) return 'bg-[#96FEAD]'
  if (progress >= 50) return 'bg-[#FFD6A5]'
  return 'bg-[#FFADAD]'
}

const getStatusColor = (status) => {
  switch(status) {
    case 'completed': return 'bg-[#96FEAD]'
    case 'in_progress': return 'bg-[#FFD6A5]'
    case 'not_started': return 'bg-[#D0F4FF]'
    default: return 'bg-gray-200'
  }
}

const getStatusText = (status) => {
  switch(status) {
    case 'completed': return 'Completado'
    case 'in_progress': return 'En Progreso'
    case 'not_started': return 'No Iniciado'
    default: return status
  }
}

const getStatusIcon = (status) => {
  switch(status) {
    case 'completed': return 'check_circle'
    case 'in_progress': return 'play_circle'
    case 'not_started': return 'radio_button_unchecked'
    default: return 'help'
  }
}
</script>

<template>
  <div class="border-2 border-black rounded-xl overflow-hidden cursor-pointer bg-white hover:scale-[101%] transition-all flex flex-col" @click="emit('click')">
    <img 
      :src="mentoria.image || '/default-course.jpg'" 
      alt="Imagen de mentoría" 
      class="w-full h-40 object-cover border-b-2 border-black" 
    />

    <div class="p-4 flex flex-col justify-between flex-1">
      <div>
        <h4 class="font-bold text-lg mb-2">{{ mentoria.title }}</h4>
        
        <!-- Mentor Info -->
        <div class="flex items-center gap-2 mb-3">
          <img 
            :src="mentoria.mentor?.profile_picture" 
            alt="Mentor" 
            class="w-6 h-6 rounded-full border border-black object-cover"
          />
          <span class="text-sm font-medium">{{ mentoria.mentor?.name }} {{ mentoria.mentor?.surname }}</span>
        </div>

        <!-- Progress Bar -->
        <div class="mb-3">
          <div class="flex justify-between items-center mb-1">
            <span class="text-sm font-medium">Progreso</span>
            <span class="text-sm font-bold">{{ mentoria.progress || 0 }}%</span>
          </div>
          <div class="w-full bg-gray-200 rounded-full h-3 border border-black">
            <div 
              :class="getProgressColor(mentoria.progress || 0)"
              class="h-full rounded-full border-r border-black transition-all duration-300"
              :style="{ width: `${mentoria.progress || 0}%` }"
            ></div>
          </div>
        </div>

        <!-- Status and Duration -->
        <div class="flex justify-between items-center mb-3">
          <NeoTab 
            :text="getStatusText(mentoria.status || 'not_started')" 
            :bg="getStatusColor(mentoria.status || 'not_started')"
            :icon="getStatusIcon(mentoria.status || 'not_started')"
          />
          <span class="text-sm font-medium text-gray-600">
            {{ mentoria.duration }}h total
          </span>
        </div>
      </div>
    </div>
  </div>
</template>