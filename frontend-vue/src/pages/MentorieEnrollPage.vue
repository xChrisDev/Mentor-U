<template>
    <div class="mx-auto flex justify-center min-h-screen" data-aos="zoom-in" data-aos-delay="100">
        <div v-if="mentorie" class="w-[90%] lg:w-[85%] pt-10">
            <!-- Mentorship Header Card -->
            <NeoContainer bg="bg-white" class="mb-8 p-6">
                <div class="grid md:grid-cols-3 gap-6">
                    <!-- Image -->
                    <div class="md:col-span-1">
                        <img :src="mentorie.image || '/default-course.jpg'" alt="Imagen de mentoría"
                            class="w-full h-74 object-cover border-2 border-black rounded-lg" />
                    </div>

                    <!-- Info -->
                    <div class="md:col-span-2 space-y-4">
                        <div>
                            <h2 class="text-2xl font-bold mb-2">{{ mentorie.title }}</h2>
                            <p class="text-gray-700">{{ mentorie.description }}</p>
                        </div>

                        <!-- Mentor Info -->
                        <div class="flex items-center gap-3 p-3 bg-[#F0F8FF] border-2 border-black rounded-lg">
                            <img :src="mentorie.mentor?.profile_picture" alt="Mentor"
                                class="w-12 h-12 rounded-full border-2 border-black object-cover" />
                            <div>
                                <h4 class="font-bold">{{ mentorie.mentor?.name }} {{ mentorie.mentor?.surname }}</h4>
                                <p class="text-sm text-gray-600">Mentor</p>
                            </div>
                        </div>

                        <!-- Stats Row -->
                        <div class="grid grid-cols-1 md:grid-cols-5 gap-3">
                            <div class="col-span-1 bg-[#D0F4FF] border-2 border-black rounded-lg p-3 text-center">
                                <span class="material-symbols-rounded text-2xl block mb-1">timer</span>
                                <div class="font-bold">{{ mentorie.duration }}h</div>
                                <div class="text-xs">Duración</div>
                            </div>

                            <div class="col-span-1 bg-[#FFD6A5] border-2 border-black rounded-lg p-3 text-center">
                                <span class="material-symbols-rounded text-2xl block mb-1">quiz</span>
                                <div class="font-bold">{{ problems?.length || 0 }}</div>
                                <div class="text-xs">Problemas</div>
                            </div>

                            <div
                                class="col-span-3 grid grid-cols-5 items-center justify-center px-4 gap-4 bg-[#E6E6FA] border-2 border-black rounded-lg">
                                <div class="flex flex-col col-span-3">
                                    <div class=" flex justify-between items-center mb-2">
                                        <span class="font-medium mr-2">Progreso General</span>
                                        <span class="font-bold text-lg">{{ mentorie.progress || 0 }}%</span>
                                    </div>
                                    <div class="bg-gray-200 rounded-full h-4 border-2 border-black">
                                        <div :class="getProgressColor(mentorie.progress || 0)"
                                            class="h-full rounded-full border-r-2 border-black transition-all duration-500"
                                            :style="{ width: `${mentorie.progress || 0}%` }"></div>
                                    </div>
                                </div>

                                <div class="flex items-center justify-center col-span-2">
                                    <NeoTab :text="getStatusText(mentorie.status || 'not_started')"
                                        :bg="getStatusColor(mentorie.status || 'not_started')"
                                        :icon="getStatusIcon(mentorie.status || 'not_started')" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </NeoContainer>

            <!-- Problems Section -->
            <NeoContainer bg="bg-[#F5F5F5]" class="p-6 flex flex-col">
                <div class="flex items-center justify-between mb-6">
                    <div class="flex items-center gap-3">
                        <span class="material-symbols-rounded text-3xl">quiz</span>
                        <h3 class="text-2xl font-bold">Problemas de la Mentoría</h3>
                    </div>

                    <!-- Filter buttons -->
                    <div class="flex gap-2">
                        <NeoButton :bg="problemFilter === 'all' ? '#96FEAD' : '#F5F5F5'" text="Todos"
                            @click="problemFilter = 'all'" />
                        <NeoButton :bg="problemFilter === 'completed' ? '#96FEAD' : '#F5F5F5'" text="Completados"
                            @click="problemFilter = 'completed'" />
                        <NeoButton :bg="problemFilter === 'pending' ? '#96FEAD' : '#F5F5F5'" text="Pendientes"
                            @click="problemFilter = 'pending'" />
                        <NeoButton :bg="problemFilter === 'in_revision' ? '#96FEAD' : '#F5F5F5'" text="En revisión"
                            @click="problemFilter = 'in_revision'" />
                    </div>
                </div>

                <!-- Problems List -->
                <div v-if="isLoadingProblems" class="flex justify-center py-8">
                    <div class="loader"></div>
                </div>

                <div v-else-if="filteredProblems?.length || 0" class="space-y-4" data-aos="fade-up" data-aos-delay="100">
                    <div v-for="(problem, index) in filteredProblems" :key="problem.id"
                        class="bg-white border-2 border-black rounded-lg p-4 hover:scale-[101%] transition-all cursor-pointer"
                        @click="openProblem(problem.id)">
                        <div class="flex items-center justify-between">
                            <div class="flex items-center gap-4 flex-1">
                                <div class="flex-1">
                                    <h4 class="font-bold text-lg mb-1">{{ problem.title }}</h4>
                                    <p class="text-gray-600 text-sm mb-2">{{ problem.description }}</p>

                                    <div class="flex gap-2 flex-wrap">
                                        <NeoTab :text="getDifficultyText(problem.difficulty)"
                                            :bg="getDifficultyColor(problem.difficulty)" icon="trending_up" />
                                        <NeoTab :text="problem.topic" bg="bg-[#E6E6FA]" icon="category" />
                                        <NeoTab :text="problem.lang" bg="bg-[#FFD6A5]" icon="code" />
                                    </div>
                                </div>
                            </div>

                            <div class="flex items-center gap-3">
                                <NeoTab :text="getStatusTabText(problem.status)" :bg="getStatusTabColor(problem.status)"
                                    :icon="getStatusTabIcon(problem.status)" />
                                <span class="material-symbols-rounded text-2xl">arrow_forward_ios</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div v-else class="flex justify-center text-md text-black py-8">
                    <NeoContainer bg="bg-white" class="w-fit">
                        No hay problemas disponibles para esta mentoría.
                    </NeoContainer>
                </div>
            </NeoContainer>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import { useToast } from 'vue-toastification';
import NeoButton from '../components/NeoButton.vue';
import NeoContainer from '../components/NeoContainer.vue';
import NeoTab from '../components/NeoTab.vue';
import { getMentorieDetailByID } from '../services/mentorieService';
import { useAuth } from '../composables/useAuth';
import { getMentoryProblemsByStudent, updateProgress } from '../services/problemService';
import { useRouter } from 'vue-router';
const { fetchUser } = useAuth();
const toast = useToast();

const router = useRouter()
const mentorie = ref(null);
const student = ref(null);
const problems = ref([]);
const isLoadingProblems = ref(false);
const problemFilter = ref('all');
const selectedProblem = ref(null);

const props = defineProps({
    id: String,
    id_mentorie: String
});

const openProblem = (id) => {
    router.push(`/home/student/${props.id}/mentories/${props.id_mentorie}/problems/${id}`)
}

const fetchMentorieDetail = async () => {
    try {
        mentorie.value = await getMentorieDetailByID(props.id_mentorie, student.value.id);
    } catch (error) {
        toast.error('Error al cargar la mentoria', { toastClassName: "my-custom-toast-class" });
    }
};

const fetchStudentData = async () => {
    const res = await fetchUser();
    student.value = res.data;
};

const fetchProblems = async () => {
    isLoadingProblems.value = true;
    try {
        problems.value = await getMentoryProblemsByStudent(props.id_mentorie, student.value.id)
    } catch (error) {
        toast.error('Error al cargar los problemas', { toastClassName: "my-custom-toast-class" });
    } finally {
        isLoadingProblems.value = false;
    }
};

// Computed properties
const filteredProblems = computed(() => {
    if (problemFilter.value === 'completed') {
        return problems.value.filter(p => p.status == 'completed');
    } else if (problemFilter.value === 'pending') {
        return problems.value.filter(p => p.status == 'pending');
    } else if (problemFilter.value === 'in_revision') {
        return problems.value.filter(p => p.status == 'in_revision');
    }
    return problems.value;
});

// Helper functions
const getStatusTabText = (status) => {
    switch (status) {
        case 'completed': return 'Completado';
        case 'pending': return 'Pendiente';
        case 'in_revision': return 'En Revisión';
        default: return 'Desconocido';
    }
};

const getStatusTabColor = (status) => {
    switch (status) {
        case 'completed': return 'bg-[#96FEAD]';
        case 'pending': return 'bg-[#FFADAD]';
        case 'in_revision': return 'bg-[#FFD6A5]';
        default: return 'bg-gray-300';
    }
};

const getStatusTabIcon = (status) => {
    switch (status) {
        case 'completed': return 'check_circle';
        case 'pending': return 'radio_button_unchecked';
        case 'in_revision': return 'hourglass_empty';
        default: return 'help';
    }
};
const getProgressColor = (progress) => {
    if (progress >= 80) return 'bg-[#96FEAD]'
    if (progress >= 50) return 'bg-[#FFD6A5]'
    return 'bg-[#FFADAD]'
};

const getStatusColor = (status) => {
    switch (status) {
        case 'completed': return 'bg-[#96FEAD]'
        case 'in_progress': return 'bg-[#FFD6A5]'
        case 'not_started': return 'bg-[#D0F4FF]'
        default: return 'bg-gray-200'
    }
};

const getStatusText = (status) => {
    switch (status) {
        case 'completed': return 'Completado'
        case 'in_progress': return 'En curso'
        case 'not_started': return 'No iniciado'
        default: return status
    }
};

const getStatusIcon = (status) => {
    switch (status) {
        case 'completed': return 'check_circle'
        case 'in_progress': return 'play_circle'
        case 'not_started': return 'radio_button_unchecked'
        default: return 'help'
    }
};

const getDifficultyColor = (difficulty) => {
    switch (difficulty) {
        case 'facil': return 'bg-[#96FEAD]';
        case 'medio': return 'bg-[#FFD6A5]';
        case 'dificil': return 'bg-[#FFADAD]';
        default: return 'bg-gray-200';
    }
};

const getDifficultyText = (difficulty) => {
    switch (difficulty) {
        case 'facil': return 'Fácil';
        case 'medio': return 'Medio';
        case 'dificil': return 'Difícil';
        default: return 'N/A';
    }
};

// const completeProblem = () => {
//     if (selectedProblem.value && !selectedProblem.value.completed) {
//         selectedProblem.value.completed = true;
//         toast.success('¡Problema completado exitosamente!', { toastClassName: "my-custom-toast-class" });

//         // Update progress
//         const completedProblems = problems.value.filter(p => p.completed).length;
//         mentorie.value.progress = Math.round((completedProblems / problems.value.length) * 100);

//         if (mentorie.value.progress === 100) {
//             mentorie.value.status = 'completed';
//             toast.success('¡Felicitaciones! Has completado toda la mentoría', { toastClassName: "my-custom-toast-class" });
//         }
//     }
//     problemModal.value?.close();
// };



onMounted(async () => {
    await fetchStudentData();
    await fetchMentorieDetail();
    await fetchProblems();
    await updateProgress(props.id_mentorie, { mentory_id: props.id_mentorie, student_id: student.value.id });
});
</script>