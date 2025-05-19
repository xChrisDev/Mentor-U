<script setup>
import { onMounted, ref } from 'vue';
import NeoContainer from '../components/NeoContainer.vue';
import MentorForm from '../components/session-page/MentorForm.vue';
import StudentForm from '../components/session-page/StudentForm.vue';
import NeoButton from '../components/NeoButton.vue';
import { useAuth } from '../composables/useAuth';
import { useRouter } from 'vue-router';

const isLoading = ref(false)
const blobColors = ['#96FEAD', '#A0C4FF', '#FFADAD', '#FFD6A5'];
const blobs = ref([]);
const isMentor = ref(true);
const {user} = useAuth()
const router = useRouter()

const handleLoading = ()=>{
        isLoading.value = !isLoading.value
}

onMounted(() => {
    blobs.value = Array.from({ length: 15 }).map(() => ({
        top: `${Math.random() * 100}%`,
        left: `${Math.random() * 100}%`,
        size: `${40 + Math.random() * 80}px`,
        duration: `${6 + Math.random() * 6}s`,
        delay: `${Math.random() * 4}s`,
        color: blobColors[Math.floor(Math.random() * blobColors.length)],
    }));

    if(user.value){
        isMentor.value = user.value.role == 'mentor'
    }else{
        router.push("/login")
    }
});

</script>

<template>
    <div v-if="isLoading" class="flex justify-center items-center h-[80dvh]">
        <div class="loader" data-aos="zoom-in" data-aos-delay="100"></div>
    </div>
    <div v-else class="fixed inset-0 z-50 flex items-center justify-center" data-aos="zoom-in" data-aos-delay="100">
        <div class="flex flex-col gap-4 justify-center items-center w-full p-8">
            <NeoContainer bg="bg-white" class="w-full max-w-3xl min-h-[550px] p-8 flex flex-col gap-6">
                <div class="flex items-center justify-between mb-2">
                    <h2 class="text-3xl font-ppgosha font-bold">{{ isMentor ? 'Registro como mentor' : 'Registro como estudiante' }}</h2>
                    <NeoButton :text="isMentor ? 'Estudiante' : 'Mentor'" bg="#F1E9FF" icon="swap_horiz" class="justify-center" @click="isMentor = !isMentor"/>
                </div>
                <div v-if="isMentor" :key="isMentor">
                    <MentorForm :role="user.role" @loading="handleLoading"/>
                </div>
                <div v-else>
                    <StudentForm :role="user.role" @loading="handleLoading"/>
                </div>
            </NeoContainer>
        </div>
    </div>

    <div class="fixed inset-0 -z-9 overflow-hidden pointer-events-none">
        <div v-for="(blob, index) in blobs" :key="index" class="absolute blob" :style="{
            top: blob.top,
            left: blob.left,
            width: blob.size,
            height: blob.size,
            backgroundColor: blob.color,
            animationDuration: blob.duration,
            animationDelay: blob.delay
        }"></div>
    </div>


</template>
