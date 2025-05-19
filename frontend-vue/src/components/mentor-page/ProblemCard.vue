<script setup>
import { onMounted, ref } from 'vue';
import NeoButton from '../NeoButton.vue';
import NeoTab from '../NeoTab.vue';

const props = defineProps({
    problem: Object
});
const level = ref(null)

const showSolution = ref(false);

onMounted(() => {
    if (props.problem.difficulty == "facil") {
        level.value = 'Fácil'
    } else if (props.problem.difficulty == "medio") {
        level.value = 'Medio'
    } else if (props.problem.difficulty == "dificil") {
        level.value = 'Difícil'
    }
})
</script>

<template>
    <div class="border-2 border-black rounded-xl p-4 bg-white ">
        <div class="flex justify-between items-center mb-2">
            <h4 class="text-xl font-bold font-ppgosha">{{ problem.title }}</h4>
            <div class="flex gap-2 mb-2">
                <NeoTab :text="problem.topic" bg="bg-[#F1E9FF]" />
                <NeoTab :text="problem.lang" bg="bg-[#D0F4FF]" />
                <NeoTab :text="level" bg="bg-[#FFD6A5]" />
            </div>
        </div>


        <p class="text-md font-medium text-gray-800 mb-2">{{ problem.description }}</p>

        <div class="border-2 border-black rounded-lg px-3 py-2 bg-[#FFF6D1] ">
            <strong class="block font-bold text-xs mb-1">Restricciones</strong>
            <p class="whitespace-pre-wrap">{{ problem.constraints }}</p>
        </div>


        <div class="flex justify-end mt-6">
            <NeoButton bg="#F1E9FF" :icon="showSolution ? 'visibility_off' : 'visibility'"
                :text="showSolution ? 'Ocultar solución' : 'Ver solución'" @click="showSolution = !showSolution" />
        </div>

        <div v-if="showSolution" class="mt-3" data-aos="fade-up" data-aos-delay="5">
            <strong>Solución esperada:</strong>
            <pre class="text-xs bg-gray-100 border border-black p-3 mt-1 overflow-x-auto whitespace-pre-wrap rounded">
{{ problem.solution }}
      </pre>
        </div>
    </div>
</template>
