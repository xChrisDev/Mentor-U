<script setup>
import { onMounted, ref, watch, computed } from 'vue';
import NeoContainer from '../components/NeoContainer.vue';
import NeoButton from '../components/NeoButton.vue';
import NeoTab from '../components/NeoTab.vue';
import { getMentorieDetailByID } from '../services/mentorieService';
import { getProblemsByMentorID } from '../services/problemService';
import ModalAddProblem from '../components/mentor-page/ModalAddProblem.vue';
import ProblemCard from '../components/mentor-page/ProblemCard.vue';
import ModalUpdateMentorie from '../components/mentor-page/ModalUpdateMentorie.vue'

const props = defineProps({
    id: String,
    id_mentorie: String
});

const mentorie = ref(null);
const problems = ref([]);

const fetchMentorieDetail = async () => {
    mentorie.value = await getMentorieDetailByID(props.id_mentorie);
    problems.value = await getProblemsByMentorID(props.id_mentorie);
    console.log(mentorie.value)
};

onMounted(fetchMentorieDetail);

// === BÚSQUEDA Y PAGINACIÓN ===
const searchQuery = ref('');
const currentPage = ref(1);
const pageSize = 3;

const filteredProblems = computed(() =>
    problems.value.filter(problem =>
        problem.title.toLowerCase().includes(searchQuery.value.toLowerCase())
    )
);

const totalPages = computed(() =>
    Math.ceil(filteredProblems.value.length / pageSize)
);

const paginatedProblems = computed(() => {
    const start = (currentPage.value - 1) * pageSize;
    return filteredProblems.value.slice(start, start + pageSize);
});

const nextPage = () => {
    if (currentPage.value < totalPages.value) currentPage.value++;
};

const prevPage = () => {
    if (currentPage.value > 1) currentPage.value--;
};

watch(searchQuery, () => {
    currentPage.value = 1;
});
</script>

<template>
    <div class="pt-6 mx-auto flex flex-col justify-center items-center gap-6" data-aos="zoom-in" data-aos-delay="100">
        <!-- MENTORIE INFO -->
        <NeoContainer class="w-full flex flex-col max-w-4xl bg-white border-2 border-black p-6">
            <div class="flex flex-col md:flex-row gap-6 w-full">
                <img :src="mentorie?.image" class="w-full md:w-48 h-48 object-cover rounded-md border-2 border-black" />

                <div class="flex flex-col w-full gap-4">

                    <div class="flex flex-col">
                        <h2 class="text-3xl font-bold font-ppgosha">{{ mentorie?.title }}</h2>
                        <div class="flex flex-wrap gap-2 mt-2">
                            <NeoTab icon="payments" :text="mentorie?.price > 0 ? `$${mentorie.price}` : 'Gratis'"
                                bg="bg-[#F1E9FF]" />
                            <NeoTab icon="schedule" :text="`Duración: ${mentorie?.duration}hr`" bg="bg-[#F1E9FF]" />
                            <NeoTab icon="groups" :text="`Máx estudiantes: ${mentorie?.max_students}`"
                                bg="bg-[#F1E9FF]" />
                        </div>
                    </div>
                    <p class="text-md font-medium">{{ mentorie?.description }}</p>
                    <div class="flex justify-end gap-2">
                        <!-- <NeoButton bg="#FFF6D1" icon="edit" /> -->
                        <div v-if="mentorie">
                            <ModalUpdateMentorie :mentorie="mentorie" @update="fetchMentorieDetail" />
                        </div>
                        <NeoButton bg="#FFADAD" icon="delete" />
                    </div>

                </div>
            </div>
        </NeoContainer>

        <!-- PROBLEMAS -->
        <NeoContainer class="w-full max-w-4xl bg-[#F1E9FF] border-2 border-black p-6 flex flex-col">
            <!-- CABECERA -->
            <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-4">
                <div class="flex items-center">
                    <span class="material-symbols-rounded text-3xl mr-2">psychology_alt</span>
                    <h3 class="text-2xl font-bold">Problemas generados</h3>
                </div>
                <ModalAddProblem :id_mentor="Number(id)" :id_mentorie="Number(id_mentorie)"
                    @update="fetchMentorieDetail" />
            </div>

            <!-- BÚSQUEDA -->
            <div class="mb-4">
                <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2">
                    <span class="material-symbols-rounded text-gray-500 me-2" style="font-size: 1.2rem;">
                        search </span>
                    <input v-model="searchQuery" type="text" placeholder="Buscar problema por título..."
                        class="w-full outline-none text-sm lg:text-base bg-transparent" />
                </div>

            </div>

            <!-- LISTA DE PROBLEMAS -->
            <div v-if="filteredProblems.length">
                <div v-for="problem in paginatedProblems" :key="problem.id" class="mb-4">
                    <ProblemCard :problem="problem" />
                </div>

                <!-- PAGINACIÓN -->
                <div class="flex justify-center items-center gap-2 mt-4">
                    <NeoButton bg="white" icon="arrow_back" @click="prevPage" :disabled="currentPage === 1" />
                    <span class="px-2 font-bold">Página {{ currentPage }} de {{ totalPages }}</span>
                    <NeoButton bg="white" icon="arrow_forward" @click="nextPage"
                        :disabled="currentPage === totalPages" />
                </div>
            </div>

            <!-- SIN PROBLEMAS -->
            <NeoContainer v-else bg="bg-white shadow-none" class="w-full flex justify-center mb-2">
                <div>
                    No hay problemas, utiliza nuestra IA para crearlos! :D
                </div>
            </NeoContainer>
        </NeoContainer>
    </div>
</template>
