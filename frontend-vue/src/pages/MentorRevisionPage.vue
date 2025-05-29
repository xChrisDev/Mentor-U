<template>
    <div v-if="submission" class="mx-auto flex justify-center py-10" data-aos="zoom-in" data-aos-delay="100">
        <div class="w-[90%] lg:w-[85%] grid grid-cols-1 lg:grid-cols-3 gap-6">

            <div class="lg:col-span-1 space-y-4">
                <div class="flex flex-col space-y-4">

                    <NeoContainer bg="bg-white" class="flex items-center gap-4">
                        <img :src="submission.student_photo" alt="Foto del estudiante"
                            class="w-14 h-14 rounded-full border-2 border-black" />
                        <div>
                            <h2 class="text-lg font-bold">{{ submission.student_name }} {{ submission.student_surname }}
                            </h2>
                            <p class="text-sm text-gray-600">ID estudiante: {{ submission.student_id }}</p>
                        </div>
                    </NeoContainer>

                    <NeoContainer bg="bg-[#F1E9FF]" class="flex flex-col gap-2 p-4">
                        <p class="text-xl"><strong>{{ submission.mentorie_title }}</strong></p>
                        <p class="font-medium text-gray-700">{{ submission.mentorie_description }}</p>
                    </NeoContainer>

                    <NeoContainer bg="bg-[#FFF6D1]" class="flex flex-col p-4">
                        <h1 class="text-xl font-bold">{{ submission.problem_title }}</h1>
                        <div class="flex gap-2 my-2">
                            <NeoTab :text="getDifficultyText(submission.problem_difficulty)"
                                :bg="getDifficultyColor(submission.problem_difficulty)" icon="trending_up" />
                            <NeoTab :text="submission.problem_topic" bg="bg-[#E6E6FA]" icon="category" />
                        </div>
                        <p class="font-medium text-gray-700">{{ submission.problem_description }}</p>
                    </NeoContainer>
                </div>
            </div>

            <div class="lg:col-span-2 space-y-4">
                <NeoContainer bg="bg-white" class="p-6 space-y-4 flex flex-col">
                    <h3 class="font-bold text-xl">Código enviado por el estudiante</h3>
                    <pre
                        class="h-64 bg-[#1A1A1A] text-white p-4 border-2 border-black rounded-lg overflow-y-auto font-mono text-xs">
{{ submission.code }}
                    </pre>


                    <div v-if="submission.result" class="mt-2">
                        <h3 class="font-bold">Estado</h3>
                        <div :class="{
                            'bg-[#96FEAD]': submission.result === 'accepted',
                            'bg-[#FFADAD]': submission.result === 'rejected',
                            'bg-[#FFF3B0]': submission.result === 'pending'
                        }" class="p-4 rounded-lg border-2 border-black">
                            <p>
                                <strong>Resultado: </strong>
                                <span :class="{
                                    'text-green-700': submission.result === 'accepted',
                                    'text-red-700': submission.result === 'rejected',
                                    'text-yellow-700': submission.result === 'pending'
                                }">
                                    {{
                                        submission.result === 'accepted'
                                            ? 'Aprobado'
                                            : submission.result === 'rejected'
                                                ? 'Devuelto'
                                                : 'En revisión'
                                    }}
                                </span>
                            </p>
                        </div>
                    </div>

                    <div>
                        <label for="mentorComments" class="font-bold mb-1 block">Comentarios</label>
                        <div class="border-2 border-black rounded-lg bg-white px-3 py-2">
                            <textarea id="mentorComments" v-model="comments" rows="5"
                                class="w-full outline-none text-sm bg-transparent resize-none"
                                placeholder="Genera retroalimentación..."></textarea>
                        </div>
                    </div>

                    <div class="flex justify-end gap-4">
                        <NeoButton text="Aprobar" bg="#96FEAD" icon="check" @click="handleApproval(true)"
                            :disabled="loading" />
                        <NeoButton text="Devolver" bg="#FFADAD" icon="close" @click="handleApproval(false)"
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
import { useToast } from 'vue-toastification';
import { getSolutionByID, updateProblemStatus, updateStudentSolution } from '../services/problemService';

const props = defineProps({
    id_solution: String,
});

const submission = ref(null);
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
    const res = await getSolutionByID(props.id_solution);
    submission.value = res;
    comments.value = res.comments || '';
});

const handleApproval = async (approved) => {
    loading.value = true;
    try {
        await updateProblemStatus(submission.value.problem_id, {
            problem_id: submission.value.problem_id,
            student_id: submission.value.student_id,
            status: approved ? 'completed' : 'pending'
        });
        await updateStudentSolution(submission.value.id, {
            code: submission.code,
            comments: comments.value,
            result: approved ? 'accepted' : 'rejected'
        })
        toast.success(`Solución ${approved ? 'aprobada' : 'devuelta'} correctamente.`, {
            toastClassName: "my-custom-toast-class",
        });
        const res = await getSolutionByID(props.id_solution);
        submission.value = res;
        comments.value = res.comments || '';
    } catch (error) {
        toast.error('Error al actualizar el estado.', {
            toastClassName: "my-custom-toast-class",
        });
    } finally {
        loading.value = false;
    }
};
</script>
