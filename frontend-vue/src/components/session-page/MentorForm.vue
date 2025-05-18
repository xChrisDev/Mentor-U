<script setup>
import { ref } from 'vue';
import NeoButton from '../NeoButton.vue';
import { useAuth } from '../../composables/useAuth';
import { updateUser } from '../../services/userService';
import { postMentor } from '../../services/mentorService';
import { useToast } from 'vue-toastification';
import { useRouter } from 'vue-router';

const techOptions = [
    { id: 1, name: 'JavaScript' },
    { id: 2, name: 'Python' },
    { id: 3, name: 'Java' },
    { id: 4, name: 'C#' },
    { id: 5, name: 'PHP' },
    { id: 6, name: 'C++' },
    { id: 7, name: 'Go' },
];

const toast = useToast()
const router = useRouter()
const emit = defineEmits('loading')
const { user } = useAuth()
const props = defineProps({
    role: String
})
const form = ref({
    name: '',
    surname: '',
    biography: '',
    specialization: '',
    genre: '',
    technologies_ids: [],
    file: null,
    preview: null
});

const isDropdownOpen = ref(false);
const genreOptions = ['Masculino', 'Femenino', 'Prefiero no decirlo'];

function selectOption(option) {
    form.value.genre = option;
    isDropdownOpen.value = false;
}

function handleFileChange(e) {
    const file = e.target.files[0];
    if (file) {
        form.value.file = file;
        form.value.preview = URL.createObjectURL(file);
    }
}

function triggerFileSelect() {
    document.getElementById('fileInput').click();
}

const handleMentorSubmit = async () => {
    console.log(user.value)
    if (props.role != 'mentor') {
        const newUser = {
            username: user.value.username,
            email: user.value.email,
            password: user.value.password,
            role: 'mentor'
        }
        const userRes = await updateUser(user.value.id, newUser)
        console.log(userRes)
    }

    let genre = ""
    if (form.value.genre === "Masculino") { genre = "male" }
    else if (form.value.genre === "Femenino") { genre = "female" }
    else if (form.value.genre === "Prefiero no decirlo") { genre = "other" }

    const formData = new FormData()
    formData.append('user_id', user.value.id)
    formData.append('name', form.value.name)
    formData.append('surname', form.value.surname)
    formData.append('biography', form.value.biography)
    formData.append('specialization', form.value.specialization)
    formData.append('genre', genre)
    formData.append('technologies_ids', form.value.technologies_ids.join(','));
    formData.append('file', form.value.file)

    emit('loading')
    const response = await postMentor(formData)
    if (response.mentor_id) {
        toast.success(response.message, {
            toastClassName: "my-custom-toast-class",
        });
        router.push('/home/mentor/' + response.mentor_id)
        emit('loading')
    } else {
        toast.error(response.message, {
            toastClassName: "my-custom-toast-class",
        });
    }
}
</script>

<template>
    <form class="flex flex-col gap-4">
        <div class="flex gap-6">
            <div>
                <!-- Imagen -->
                <div class="flex flex-col gap-1 w-full">
                    <label class="font-semibold text-sm lg:text-base"> Foto de perfil </label>
                    <div class="flex items-center justify-center hover:grayscale transition-all border-[3px] border-black rounded-xl bg-white w-32 h-32 cursor-pointer relative overflow-hidden"
                        @click="triggerFileSelect">
                        <input id="fileInput" type="file" accept="image/*" @change="handleFileChange" class="hidden" />
                        <img v-if="form.preview" :src="form.preview" alt="Preview" class="w-full h-full object-cover" />
                        <span v-else class="material-symbols-rounded text-4xl text-gray-500"> image </span>
                    </div>
                </div>
            </div>
            <div class="flex flex-col gap-2 w-full">
                <!-- Nombre -->
                <div class="flex flex-col gap-1 w-full">
                    <label class="font-semibold text-sm lg:text-base" for="name"> Nombre(s) </label>
                    <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2">
                        <span class="material-symbols-rounded text-gray-500 me-2" style="font-size: 1.2rem;">
                            account_circle </span>
                        <input id="name" type="text" placeholder="Arthur" v-model="form.name"
                            class="w-full outline-none text-sm lg:text-base bg-transparent" autocomplete="off" />
                    </div>
                </div>

                <!-- Apellido -->
                <div class="flex flex-col gap-1 w-full">
                    <label class="font-semibold text-sm lg:text-base" for="surname"> Apellido(s) </label>
                    <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2">
                        <span class="material-symbols-rounded text-gray-500 me-2" style="font-size: 1.2rem;">
                            account_circle </span>
                        <input id="surname" type="text" placeholder="Morgan" v-model="form.surname"
                            class="w-full outline-none text-sm lg:text-base bg-transparent" autocomplete="off" />
                    </div>
                </div>
            </div>

            <div class="flex flex-col gap-2 w-full">
                <!-- Género -->
                <div class="flex flex-col gap-1 w-full relative">
                    <label class="font-semibold text-sm lg:text-base"> Género </label>

                    <!-- Caja principal -->
                    <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2 relative cursor-pointer"
                        @click="isDropdownOpen = !isDropdownOpen">
                        <span class="material-symbols-rounded text-gray-500 me-2" style="font-size: 1.2rem;">
                            diversity_3 </span>
                        <span class="text-sm lg:text-base select-none">
                            {{ form.genre || 'Selecciona una opción' }}
                        </span>
                        <span class="material-symbols-rounded absolute right-4 text-gray-500"> expand_more </span>
                    </div>

                    <!-- Opciones -->
                    <div v-show="isDropdownOpen"
                        class="absolute top-full mt-2 left-0 right-0 border-[3px] border-black rounded-xl bg-white z-50">
                        <div v-for="option in genreOptions" :key="option" @click="selectOption(option)"
                            class="px-4 py-2 rounded-xl cursor-pointer hover:bg-gray-200 text-sm lg:text-base border-black last:border-none">
                            {{ option }}
                        </div>
                    </div>
                </div>

                <!-- Especialidad -->
                <div class="flex flex-col gap-1 w-full">
                    <label class="font-semibold text-sm lg:text-base" for="specialization"> Especialidad </label>
                    <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2">
                        <span class="material-symbols-rounded text-gray-500 me-2" style="font-size: 1.2rem;"> work
                        </span>
                        <input id="specialization" type="text" placeholder="Frontend, Backend, Data..."
                            v-model="form.specialization"
                            class="w-full outline-none text-sm lg:text-base bg-transparent" autocomplete="off" />
                    </div>
                </div>
            </div>
        </div>

        <!-- Tecnologías -->
        <div class="flex flex-col gap-1 w-full">
            <label class="font-semibold text-sm lg:text-base"> Lenguajes / Tecnologías </label>
            <div class="flex gap-2">
                <label v-for="tech in techOptions" :key="tech.id"
                    class="flex w-full items-center gap-2 border-[3px] border-black rounded-xl bg-white px-4 py-2 cursor-pointer hover:bg-gray-100 transition-all">
                    <input type="checkbox" :value="tech.id" class="accent-black w-3 h-3"
                        v-model="form.technologies_ids" />
                    <span class="text-sm">{{ tech.name }}</span>
                </label>
            </div>
        </div>


        <!-- Biografía (Textarea) -->
        <div class="flex flex-col gap-1 w-full">
            <label class="font-semibold text-sm lg:text-base" for="biography"> Biografía </label>
            <div class="border-[3px] border-black rounded-xl bg-white px-4 py-2">
                <textarea id="biography" rows="4" placeholder="Cuéntanos sobre ti..." v-model="form.biography"
                    class="w-full outline-none text-sm lg:text-base bg-transparent resize-none"></textarea>
            </div>
        </div>

        <NeoButton @click="handleMentorSubmit" text="Continuar como mentor" bg="#FDD965" icon="arrow_forward"
            class="mt-4 justify-center" />
    </form>
</template>
