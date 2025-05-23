<script setup>
import { onMounted, ref } from 'vue';
import NeoButton from '../NeoButton.vue';
import NeoTab from '../NeoTab.vue';

const props = defineProps({
    problem: Object
});

const level = ref(null);
const showSolution = ref(false);
const showExamples = ref(false);

onMounted(() => {
    if (props.problem.difficulty == "facil") {
        level.value = 'Fácil';
    } else if (props.problem.difficulty == "medio") {
        level.value = 'Medio';
    } else if (props.problem.difficulty == "dificil") {
        level.value = 'Difícil';
    }
});
</script>

<template>
    <div class="border-2 border-black rounded-xl p-4 bg-white">
        <div class="flex justify-between items-center mb-2">
            <h4 class="text-xl font-bold font-ppgosha">{{ problem.title }}</h4>
            <div class="flex gap-2 mb-2">
                <NeoTab :text="problem.topic" bg="bg-[#F1E9FF]" />
                <NeoTab :text="problem.lang" bg="bg-[#D0F4FF]" />
                <NeoTab :text="level" bg="bg-[#FFD6A5]" />
            </div>
        </div>

        <p class="text-md font-medium text-gray-800 mb-2">{{ problem.description }}</p>

        <h5 class="text-md font-bold">Restricciones</h5>
        <div class="border-2 border-black rounded-lg px-3 py-2 bg-[#FFF6D1] mb-4 mt-2">
            <p class="text-sm whitespace-pre-wrap font-medium">{{ problem.constraints }}</p>
        </div>

        <!-- BOTÓN DE EJEMPLOS -->
        <div class="flex justify-end mt-4">
            <NeoButton 
                v-if="problem.examples && problem.examples.length"
                bg="#D0F4FF" 
                :icon="showExamples ? 'visibility_off' : 'visibility'"
                :text="showExamples ? 'Ocultar ejemplos' : 'Ver ejemplos'" 
                @click="showExamples = !showExamples" 
            />
        </div>

        <!-- EJEMPLOS -->
        <div v-if="showExamples && problem.examples.length" class="space-y-4 mb-2 mt-4" data-aos="fade-up" data-aos-delay="5">
            <h5 class="text-md font-bold">Ejemplos</h5>
            <div 
                v-for="example in problem.examples" 
                :key="example.id"
                class="border-2 border-black rounded-xl bg-[#D0F4FF] p-4 space-y-3"
            >
                <div>
                    <p class="text-sm font-bold mb-1">Entrada:</p>
                    <div class="bg-white border border-black rounded p-2 text-sm font-mono text-gray-800">
                        {{ example.input }}
                    </div>
                </div>

                <div>
                    <p class="text-sm font-bold mb-1">Salida esperada:</p>
                    <div class="bg-white border border-black rounded p-2 text-sm font-mono text-gray-800">
                        {{ example.output }}
                    </div>
                </div>

                <div>
                    <p class="text-sm font-bold mb-1">Explicación:</p>
                    <div class="bg-[#fefce8] border border-black rounded p-2 text-sm text-gray-700">
                        {{ example.explanation }}
                    </div>
                </div>
            </div>
        </div>

        <!-- BOTÓN DE SOLUCIÓN -->
        <div class="flex justify-end mt-4">
            <NeoButton 
                bg="#F1E9FF" 
                :icon="showSolution ? 'visibility_off' : 'visibility'"
                :text="showSolution ? 'Ocultar solución' : 'Ver solución'" 
                @click="showSolution = !showSolution" 
            />
        </div>

        <!-- SOLUCIÓN -->
        <div v-if="showSolution" class="mt-3" data-aos="fade-up" data-aos-delay="5">
            <strong>Solución esperada:</strong>
            <pre class="text-xs bg-gray-100 border border-black p-3 mt-1 overflow-x-auto whitespace-pre-wrap rounded">
{{ problem.solution }}
            </pre>
        </div>
    </div>
</template>
