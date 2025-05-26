<template>
  <div class="mx-auto flex justify-center items-center" data-aos="zoom-in" data-aos-delay="100">
    <div v-if="student" class="w-[90%] lg:w-[85%] pt-10">
      <!-- Header -->
      <div class="flex justify-end md:justify-between items-center mb-12">
        <div class="hidden md:flex md:flex-col">
          <div class="flex items-center gap-4">
            <img :src="student?.profile_picture || '/default-avatar.png'" alt="Profile"
              class="w-22 h-full object-cover border-2 rounded-full" />
            <div>
              <h1 class="text-4xl font-ppgosha font-bold mb-1 flex items-center gap-3">
                ¡Hola, {{ student?.name }} {{ student?.surname }}!
                <span style="font-size: 2.5rem;" class="material-symbols-rounded">school</span>
              </h1>
              <p class="text-lg">Descubre nuevas mentorías y continúa aprendiendo.</p>
            </div>
          </div>
        </div>
        <div class="flex gap-4">
          <ModalSettingsUser :student="student" @settings="fetchLogout" />
          <NeoButton icon="logout" bg="#FFADAD" @click="fetchLogout" />
        </div>
      </div>

      <!-- Navigation Tabs -->
      <div class="flex justify-between mb-6">
        <div class="flex gap-2">
          <NeoButton :bg="activeTab === 'discover' ? '#96FEAD' : '#F5F5F5'" text="Descubrir" icon="explore"
            @click="activeTab = 'discover'" />
          <NeoButton :bg="activeTab === 'enrolled' ? '#96FEAD' : '#F5F5F5'" text="Mis Mentorías" icon="bookmark"
            @click="activeTab = 'enrolled'" />
        </div>

        <div class="flex gap-2">
          <div class="relative group">
            <NeoContainer bg="bg-[#EBDFFF]" class="flex items-center justify-center px-4 cursor-default">
              <span class="material-symbols-rounded mr-2">school</span>
              <h3 class="text-xl font-extrabold">{{ enrolledMentories.length }}
              </h3>
            </NeoContainer>

            <div class="absolute -top-10 left-1/2 -translate-x-1/2 invisible group-hover:visible opacity-0 group-hover:opacity-100 transition-all
    bg-white border-[3px] border-black text-sm font-semibold px-3 py-1 rounded-xl z-10 whitespace-nowrap">
              Mentorías inscritas
            </div>
          </div>

          <div class="relative group">
            <NeoContainer bg="bg-[#FFD6A5]" class="flex items-center justify-center px-4 cursor-default">
              <span class="material-symbols-rounded mr-2">workspace_premium</span>
              <h3 class="text-xl font-extrabold">0
              </h3>
            </NeoContainer>

            <div class="absolute -top-10 left-1/2 -translate-x-1/2 invisible group-hover:visible opacity-0 group-hover:opacity-100 transition-all
    bg-white border-[3px] border-black text-sm font-semibold px-3 py-1 rounded-xl z-10 whitespace-nowrap">
              Certificados obtenidos
            </div>
          </div>

        </div>
      </div>

      <!-- Discover Tab -->
      <div v-if="activeTab === 'discover'">
        <NeoContainer bg="bg-[#D0F4FF]" class="flex flex-col p-6 mb-6">
          <div class="flex justify-between items-center mb-4">
            <div class="flex items-center">
              <span class="material-symbols-rounded text-3xl mr-3">explore</span>
              <h3 class="text-2xl font-bold">Descubre mentorías</h3>
            </div>
            <!-- SearchBar -->
            <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2 w-64">
              <span class="material-symbols-rounded text-gray-500 mr-2">search</span>
              <input v-model="searchQuery" type="text" placeholder="Buscar mentoría..."
                class="w-full outline-none text-sm bg-transparent" />
            </div>
          </div>

          <div v-if="isLoading" class="flex justify-center py-8">
            <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-black"></div>
          </div>

          <div v-else-if="filteredMentories.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <StudentMentorieCard v-for="mentorie in filteredMentories" :key="mentorie.id" :mentoria="mentorie"
              @enroll="handleMentorieEnroll(mentorie.id)" />
          </div>

          <div v-else class="flex justify-center text-md text-black py-8">
            <NeoContainer bg="bg-white" class="w-fit">
              No se encontraron mentorías que coincidan con tu búsqueda.
            </NeoContainer>
          </div>
        </NeoContainer>
      </div>

      <!-- Enrolled Tab -->
      <div v-if="activeTab === 'enrolled'">
        <NeoContainer bg="bg-[#F1E9FF]" class="p-6 flex flex-col">
          <div class="flex items-center mb-4 justify-between">
            <div class="flex items-center">
              <span class="material-symbols-rounded text-3xl mr-3">bookmark</span>
              <h3 class="text-2xl font-bold">Mis mentorías</h3>
            </div>
            <!-- SearchBar -->
            <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2 w-64">
              <span class="material-symbols-rounded text-gray-500 mr-2">search</span>
              <input v-model="searchQuery" type="text" placeholder="Buscar mentoría..."
                class="w-full outline-none text-sm bg-transparent" />
            </div>
          </div>

          <div v-if="filteredEnrolledMentories.length" class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <EnrolledMentorieCard v-for="mentorie in filteredEnrolledMentories" :key="mentorie.id" :mentoria="mentorie"
              @click="handleMentorieDetails(mentorie.id)" />
          </div>

          <div v-else class="flex justify-center text-md text-black py-8">
            <NeoContainer bg="bg-white" class="w-fit">
              Aún no te has inscrito en ninguna mentoría o no hay coincidencias con tu búsqueda.
            </NeoContainer>
          </div>
        </NeoContainer>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import NeoButton from '../components/NeoButton.vue';
import NeoContainer from '../components/NeoContainer.vue';
import StudentMentorieCard from '../components/student-page/StudentMentorieCard.vue';
import EnrolledMentorieCard from '../components/student-page/EnrolledMentorieCard.vue';

import { useAuth } from '../composables/useAuth';
import { useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';
import { getAllMentories, enrollMentorie, getAllMentoriesByStudent } from '../services/mentorieService';
import ModalSettingsUser from '../components/student-page/ModalSettingsUser.vue';

const { clearUser, fetchUser, logout } = useAuth();
const toast = useToast();
const router = useRouter();

const student = ref(null);
const allMentories = ref([]);
const enrolledMentories = ref([]);
const activeTab = ref('enrolled');
const isLoading = ref(false);
const searchQuery = ref('');

const props = defineProps({ id: String });

const fetchStudentData = async () => {
  const res = await fetchUser();
  student.value = res.data;
};

const fetchLogout = async () => {
  const res = await logout();
  toast.success(res.data.message, { toastClassName: "my-custom-toast-class" });
  router.push("/login");
};

const fetchAllMentories = async () => {
  isLoading.value = true;
  try {
    const res = await getAllMentories(student.value.id);
    allMentories.value = res;
  } catch {
    toast.error('Error al cargar las mentorías');
  } finally {
    isLoading.value = false;
  }
};

const fetchEnrolledMentories = async () => {
  isLoading.value = true;
  try {
    const res = await getAllMentoriesByStudent(student.value.id);
    enrolledMentories.value = res;
  } catch {
    toast.error('Error al cargar las mentorías');
  } finally {
    isLoading.value = false;
  }
};

const handleMentorieEnroll = async (mentorieId) => {
  try {
    const data = {
      mentory_id: mentorieId,
      student_id: student.value.id,
      progress: 0,
      status: "not_started"
    };
    const res = await enrollMentorie(data);
    if (res.message) {
      toast.success('¡Te has inscrito exitosamente!', { toastClassName: "my-custom-toast-class" });
      await fetchAllMentories();
      await fetchEnrolledMentories();
    }
  } catch {
    toast.error('Error al inscribirse a la mentoría', { toastClassName: "my-custom-toast-class" });
  }
};

const handleMentorieDetails = (mentorieId) => {
  router.push(`/home/student/${props.id}/mentories/${mentorieId}`);
};

const filteredMentories = computed(() =>
  allMentories.value.filter(m =>
    m.title.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
);

const filteredEnrolledMentories = computed(() =>
  enrolledMentories.value.filter(m =>
    m.title.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
);

onMounted(async () => {
  clearUser();
  await fetchStudentData();
  await fetchAllMentories();
  await fetchEnrolledMentories();
});
</script>
