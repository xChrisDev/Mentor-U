<script setup>
import { onMounted, ref, computed } from 'vue';
import NeoButton from '../components/NeoButton.vue';
import NeoContainer from '../components/NeoContainer.vue';
import NeoTab from '../components/NeoTab.vue';
import { useAuth } from '../composables/useAuth';
import { useToast } from 'vue-toastification';
import { useRouter } from 'vue-router';
import MentorieCard from '../components/mentor-page/MentorieCard.vue';
import { getTechsByID } from '../services/mentorService';
import { getMentorieByID, getMentorStudentCount } from '../services/mentorieService';
import ModalAddMentorie from '../components/mentor-page/ModalAddMentorie.vue';
import ModalSettingsUser from '../components/mentor-page/ModalSettingsUser.vue';
import { getSolutionsByMentorID } from '../services/problemService';
import SolutionCard from '../components/mentor-page/SolutionCard.vue';

const { clearUser, fetchUser, logout } = useAuth()
const toast = useToast()
const router = useRouter()
const mentories = ref([])
const solutions = ref([])
const techs = ref([])
const mentor = ref(null)
const studentCount = ref(0)

const mentorieSearch = ref('')
const solutionFilter = ref('all')

const props = defineProps({
  id: String
})

const fetchLogout = async () => {
  const res = await logout()
  toast.success(res.data.message, {
    toastClassName: "my-custom-toast-class",
  });
  router.push("/login")
}

const fetchMentorData = async () => {
  const res = await fetchUser();
  mentor.value = res.data
  const response = await getMentorStudentCount(mentor.value.id)
  studentCount.value = response.students_count
}

const fetchMentories = async () => {
  const res = await getMentorieByID(mentor.value.id)
  mentories.value = res
}

const fetchMentorAndStudentsProblems = async () => {
  const res = await getSolutionsByMentorID(mentor.value.id)
  solutions.value = res
}

const fetchMentorTechs = async () => {
  const res = await getTechsByID(mentor.value.id)
  techs.value = res
}

const handleMentorieDetails = (mentorie_id) => {
  router.push(`/home/mentor/${mentor.value.user_id}/mentories/${mentorie_id}`);
}

const handleProblemDetails = (solution_id, mentorie_id) => {
  router.push(`/home/mentor/${mentor.value.user_id}/mentories/${mentorie_id}/solutions/${solution_id}`);
}

const filteredMentories = computed(() => {
  return mentories.value.filter(m =>
    m.title.toLowerCase().includes(mentorieSearch.value.toLowerCase())
  )
})

const filteredSolutions = computed(() => {
  if (solutionFilter.value === 'all') return solutions.value
  return solutions.value.filter(s => s.result === solutionFilter.value)
})

onMounted(async () => {
  clearUser();
  await fetchMentorData();
  await fetchMentories();
  await fetchMentorTechs();
  await fetchMentorAndStudentsProblems();
});
</script>

<template>
  <div class="mx-auto flex justify-center items-center" data-aos="zoom-in" data-aos-delay="100">
    <div v-if="mentor" class="w-[75%] pt-10">
      <div class="flex justify-end md:justify-between items-center mb-4">
        <div class="hidden md:flex md:flex-col">
          <div class="flex items-center gap-4">
            <NeoContainer class="flex items-center gap-4" bg="bg-white">
              <img src="/favicon.png" class="h-10" alt="favicon">
            </NeoContainer>
            <div>
              <h1 class="text-4xl font-ppgosha font-bold mb-1 flex items-center gap-3">¡Hola, {{ mentor?.name ||
                'Mentor' }}! <span style="font-size: 2.5rem;" class="material-symbols-rounded">
                  waving_hand
                </span></h1>
              <p class="text-lg">Gestiona tus mentorías y comparte tu conocimiento.</p>
            </div>
          </div>
        </div>
        <div class="flex gap-4">
          <ModalAddMentorie :id_mentor="mentor.id" @update="fetchMentories" />
          <ModalSettingsUser :mentor="mentor" @settings="fetchLogout" />
          <NeoButton icon="logout" bg="#FFADAD" @click="fetchLogout" />
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mt-6">
        <NeoContainer bg="bg-white" class="flex flex-col md:flex-row items-center p-6 col-span-1 md:col-span-3">
          <div class="flex-shrink-0 mb-4 md:mb-0 md:mr-6">
            <div class="w-32 h-32 rounded-md border-2 border-black overflow-hidden">
              <img :src="mentor?.profile_picture" alt="Profile" class="w-full h-full object-cover" />
            </div>
          </div>
          <div>
            <h3 class="text-xl font-bold">
              {{ mentor?.name }} {{ mentor?.surname }}
            </h3>
            <p class="text-md mt-1">{{ mentor?.specialization }}</p>
            <p class="text-sm font-medium mt-2">{{ mentor?.biography }}</p>
            <div class="flex flex-wrap gap-2 mt-3">
              <NeoTab v-for="tech in techs" bg="bg-[#F1E9FF]" icon="code" :text="tech" />
            </div>
          </div>
        </NeoContainer>
        <NeoContainer bg="bg-[#F1E9FF]" class="flex flex-col items-center p-6">
          <span class="material-symbols-rounded text-3xl mb-2" style="font-size: 3em;">groups</span>
          <h3 class=" text-xl font-bold">Estudiantes</h3>
          <p class="text-3xl font-bold mt-2">
            {{ studentCount || 0 }}
          </p>
        </NeoContainer>
      </div>

      <NeoContainer bg="bg-[#FFF6D1]" class="p-6 mt-8 flex flex-col w-full">
        <div class="flex justify-between items-center mb-4 gap-4">
          <div class="flex items-center">
            <span class="material-symbols-rounded me-2" style="font-size: 2em;">menu_book</span>
            <h3 class="text-2xl font-bold">Tus mentorías</h3>
          </div>
          <input type="text" v-model="mentorieSearch" placeholder="Buscar por título..."
            class="border-2 bg-white border-black px-4 py-2 rounded-md w-96" />
        </div>

        <div v-if="filteredMentories.length" class="grid grid-cols-1 md:grid-cols-2 gap-5">
          <MentorieCard v-for="mentorie in filteredMentories" :key="mentorie.id" :mentoria="mentorie"
            @click="handleMentorieDetails(mentorie.id)" />
        </div>
        <div v-else class="flex justify-center text-md text-black mt-4">
          <NeoContainer bg="bg-white shadow-none" class="w-fit mb-2">
            No se encontraron mentorías con ese título.
          </NeoContainer>
        </div>
      </NeoContainer>

      <NeoContainer bg="bg-[#FFF6D1]" class="p-6 mt-8 flex flex-col w-full">
        <div class="flex items-center justify-between gap-2 mb-4">
          <div class="flex gap-2">
            <span class="material-symbols-rounded text-3xl" style="font-size: 2em;">assignment_turned_in</span>
            <h3 class="text-2xl font-bold">Tus revisiones</h3>
          </div>
          <div class="flex gap-2">
            <NeoTab class="hover:scale-105 transition-all cursor-pointer" :bg="solutionFilter === 'all' ? 'bg-green-300' : 'bg-white'" text="Todas" :active="solutionFilter === 'all'" @click="solutionFilter = 'all'" />
            <NeoTab class="hover:scale-105 transition-all cursor-pointer" :bg="solutionFilter === 'accepted' ? 'bg-green-300' : 'bg-white'" text="Aceptadas" :active="solutionFilter === 'accepted'" @click="solutionFilter = 'accepted'" />
            <NeoTab class="hover:scale-105 transition-all cursor-pointer" :bg="solutionFilter === 'pending' ? 'bg-green-300' : 'bg-white'" text="Pendientes" :active="solutionFilter === 'pending'" @click="solutionFilter = 'pending'" />
            <NeoTab class="hover:scale-105 transition-all cursor-pointer" :bg="solutionFilter === 'rejected' ? 'bg-green-300' : 'bg-white'" text="Devueltas" :active="solutionFilter === 'rejected'" @click="solutionFilter = 'rejected'" />
          </div>
        </div>
        <div v-if="filteredSolutions.length" class="grid grid-cols-1 md:grid-cols-2 gap-5">
          <SolutionCard v-for="solution in filteredSolutions" :key="solution.id" :data="solution"
            @click="handleProblemDetails(solution.id, solution.mentorie_id)" />
        </div>
        <div v-else class="flex justify-center text-md text-black mt-4">
          <NeoContainer bg="bg-white shadow-none" class="w-fit mb-2">
            No hay soluciones con ese estado.
          </NeoContainer>
        </div>
      </NeoContainer>
    </div>
  </div>
</template>
