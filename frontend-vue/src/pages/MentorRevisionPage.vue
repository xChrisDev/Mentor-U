<template>
    <div v-if="problem" class="mx-auto flex justify-center py-10" data-aos="zoom-in" data-aos-delay="100">
        <div class="w-[90%] lg:w-[85%] grid grid-cols-1 lg:grid-cols-3 gap-6">

            <div class="lg:col-span-1 space-y-4">
                <NeoContainer bg="bg-white" class="flex flex-col p-6 space-y-4">
                    <div>
                        <h1 class="text-2xl font-bold">{{ problem.title }}</h1>
                        <div class="flex gap-2 my-2">
                            <NeoTab :text="getDifficultyText(problem.difficulty)"
                                :bg="getDifficultyColor(problem.difficulty)" icon="trending_up" />
                            <NeoTab :text="problem.topic" bg="bg-[#E6E6FA]" icon="category" />
                            <NeoTab :text="problem.lang" bg="bg-[#FFD6A5]" icon="code" />
                        </div>
                        <p class="font-medium text-gray-700">{{ problem.description }}</p>
                    </div>

                    <div>
                        <h3 class="font-bold mb-2">Restricciones</h3>
                        <NeoContainer bg="bg-[#EBDFFF]" class="p-4 border border-black shadow-none">
                            <p class="text-md text-gray-600">{{ problem.constraints }}</p>
                        </NeoContainer>
                    </div>

                    <div v-if="problem.examples.length">
                        <h3 class="font-bold mb-2">Ejemplos</h3>
                        <div v-for="(ex, i) in problem.examples" :key="i"
                            class="bg-[#FFEECE] border-2 border-black rounded-lg p-4 mb-2">
                            <p><strong>Entrada:</strong> {{ ex.input }}</p>
                            <p><strong>Salida esperada:</strong> {{ ex.output }}</p>
                        </div>
                    </div>
                </NeoContainer>
            </div>

            <div class="lg:col-span-2 space-y-4">
                <NeoContainer bg="bg-white" class="p-6 space-y-4 flex flex-col">
                    <h3 class="font-bold text-xl">Código enviado por el estudiante</h3>
                    <MonacoEditor :value="studentCode" :language="problem.lang.toLowerCase() || 'javascript'"
                        :options="{ readOnly: true }" />

                    <div v-if="result" class="mt-4">
                        <h3 class="font-bold">Resultados de la prueba</h3>
                        <div v-if="Array.isArray(result.message.results)">
                            <div v-for="(test, i) in result.message.results" :key="i" class="border rounded-lg p-4 my-2"
                                :class="test.passed ? 'bg-[#96FEAD]' : 'bg-[#FFADAD]'">
                                <p><strong>#{{ i + 1 }}</strong></p>
                                <p><strong>Entrada:</strong> {{ test.input }}</p>
                                <p><strong>Salida esperada:</strong> {{ test.expected_output }}</p>
                                <p><strong>Salida obtenida:</strong> {{ test.actual_output }}</p>
                                <p>
                                    <strong>Resultado:</strong>
                                    <span :class="test.passed ? 'text-green-700' : 'text-red-700'">
                                        {{ test.passed ? 'Correcto' : 'Incorrecto' }}
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>

                    <div>
                        <label for="mentorComments" class="font-bold mb-1 block">Comentarios del mentor</label>
                        <textarea id="mentorComments" v-model="comments" rows="5"
                            class="w-full border border-gray-400 rounded p-2"></textarea>
                    </div>

                    <div class="flex justify-end gap-4">
                        <NeoButton text="Aprobar" bg="#96FEAD" icon="check" @click="handleApproval(true)"
                            :disabled="loading" />
                        <NeoButton text="Rechazar" bg="#FFADAD" icon="close" @click="handleApproval(false)"
                            :disabled="loading" />
                    </div>

                    <div v-if="loading" class="loader"></div>
                </NeoContainer>
            </div>

        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import NeoContainer from '../components/NeoContainer.vue';
import NeoButton from '../components/NeoButton.vue';
import NeoTab from '../components/NeoTab.vue';
import MonacoEditor from '../components/MonacoEditor.vue';
import { getProblemByID } from '../services/problemService';
import { useToast } from 'vue-toastification';

const props = defineProps({
    id_problem: String,
    student_id: String, 
});

const problem = ref(null);
const studentCode = ref('');
const result = ref(null);
const comments = ref('');
const loading = ref(false);
const toast = useToast();

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

onMounted(async () => {
    problem.value = await getProblemByID(props.id_problem);
    // Obtener la solución enviada por el estudiante
    const submission = await getProblemByID(props.id_problem, res.data.id)
    if (submission) {
        studentCode.value = submission.code;
        result.value = submission.result;
        comments.value = submission.mentor_comments || '';
    }
});

const handleApproval = async (approved) => {
    loading.value = true;
    try {
        const res = await updateProblemStatus(props.id_problem, { problem_id: props.id_problem, student_id: user.data.id, status: approved ? 'completed' : 'pending' })
        // toast.success(`Solución ${approved ? 'aprobada' : 'rechazada'} correctamente.`);
    } catch (error) {
        // toast.error('Error al actualizar el estado.');
    } finally {
        loading.value = false;
    }
};
</script>
