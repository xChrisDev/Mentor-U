<script setup>
import { onMounted, ref } from 'vue';
import NeoButton from '../NeoButton.vue';
import NeoModal from '../NeoModal.vue';
import { useToast } from 'vue-toastification';
import { updateUser, getUser } from '../../services/userService';
import { putStudent } from '../../services/studentService';

const props = defineProps({
    student: Object
});

const emit = defineEmits(['settings']);
const toast = useToast();
const modalRef = ref(null);
const isLoading = ref(false);

const form = ref({
    user_id: props.student.user_id,
    name: props.student.name,
    surname: props.student.surname,
    genre: props.student.genre === 'male' ? 'Masculino' :
        props.student.genre === 'female' ? 'Femenino' : 'Prefiero no decirlo',
    username: '',
    email: '',
    password: '',
    file: null,
    preview: props.student.profile_picture
});

const isDropdownOpen = ref(false);
const genreOptions = ['Masculino', 'Femenino', 'Prefiero no decirlo'];

function handleFileChange(e) {
    const file = e.target.files[0];
    if (file) {
        form.value.file = file;
        form.value.preview = URL.createObjectURL(file);
    }
}

function triggerFileSelect() {
    document.getElementById('fileInput2').click();
}

function selectOption(option) {
    form.value.genre = option;
    isDropdownOpen.value = false;
}

function openModal() {
    modalRef.value?.open();
}

async function handleConfirm() {
    isLoading.value = true;

    try {
        const newUser = {
            username: form.value.username,
            email: form.value.email,
            password: form.value.password,
            role: 'student'
        };

        const userRes = await updateUser(form.value.user_id, newUser);
        if (userRes.error) {
            toast.error(userRes.error, {
                toastClassName: "my-custom-toast-class",
            });
            return;
        }

        const genre = mapGenre(form.value.genre);

        const formData = new FormData();
        formData.append('user_id', form.value.user_id);
        formData.append('name', form.value.name);
        formData.append('surname', form.value.surname);
        formData.append('genre', genre);

        if (form.value.file) {
            formData.append('file', form.value.file);
        }

        const response = await putStudent(props.student.id, formData);
        if (response.student_id) {
            toast.success(response.message, {
                toastClassName: "my-custom-toast-class",
            });
            emit('settings');
        } else {
            toast.error(response.message, {
                toastClassName: "my-custom-toast-class",
            });
        }
    } catch (error) {
        toast.error('Ocurrió un error inesperado', {
            toastClassName: "my-custom-toast-class",
        });
        console.error(error);
    } finally {
        isLoading.value = false;
        modalRef.value?.close();
    }
}

function mapGenre(input) {
    const map = {
        "Masculino": "male",
        "Femenino": "female",
        "Prefiero no decirlo": "other"
    };
    return map[input] || "other";
}

onMounted(async () => {
    const res = await getUser(props.student.user_id);
    form.value.username = res.username;
    form.value.email = res.email;
});
</script>

<template>
    <div>
        <NeoButton icon="settings" bg="#DDD" @click="openModal" />

        <NeoModal ref="modalRef" title="Mi cuenta" icon="account_circle" bg="#A0C4FF" @confirm="handleConfirm">
            <form class="flex flex-col gap-4">
                <div class="grid grid-cols-8 gap-4">
                    <!-- Foto -->
                    <div class="col-span-2 flex flex-col gap-1 items-center md:items-start">
                        <label class="font-semibold text-sm lg:text-base"> Foto </label>
                        <div class="flex items-center justify-center hover:grayscale transition-all border-[3px] border-black rounded-xl bg-white w-31 h-31 cursor-pointer relative overflow-hidden"
                            @click="triggerFileSelect">
                            <input id="fileInput2" type="file" accept="image/*" @change="handleFileChange"
                                class="hidden" />
                            <img v-if="form.preview" :src="form.preview" alt="Preview"
                                class="w-full h-full object-cover" />
                            <span v-else class="material-symbols-rounded text-2xl text-gray-500"> image </span>
                        </div>
                    </div>

                    <div class="col-span-3 flex flex-col gap-1">
                        <!-- Nombre -->
                        <div class="flex flex-col gap-1">
                            <label class="font-semibold text-sm lg:text-base" for="name"> Nombre(s) </label>
                            <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-3 py-2">
                                <span class="material-symbols-rounded text-gray-500 me-2 text-lg"> account_circle
                                </span>
                                <input id="name" type="text" placeholder="Nombre" v-model="form.name"
                                    class="w-full outline-none text-sm bg-transparent" autocomplete="off" />
                            </div>
                        </div>

                        <!-- Email -->
                        <div class="flex flex-col w-full gap-1">
                            <label class="font-semibold text-sm lg:text-base" for="email"> Email </label>
                            <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2">
                                <span class="material-symbols-rounded text-gray-500 me-2" style="font-size: 1.2rem;">
                                    email
                                </span>
                                <input id="email" type="email" placeholder="ejemplo@correo.com" v-model="form.email"
                                    class="w-full outline-none text-sm lg:text-base bg-transparent"
                                    autocomplete="off" />
                            </div>
                        </div>



                    </div>

                    <div class="col-span-3 flex flex-col gap-1">
                        <!-- Apellido -->
                        <div class=" col-span-2 flex flex-col gap-1">
                            <label class="font-semibold text-sm lg:text-base" for="surname"> Apellido(s) </label>
                            <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-3 py-2">
                                <span class="material-symbols-rounded text-gray-500 me-2 text-lg"> account_circle
                                </span>
                                <input id="surname" type="text" placeholder="Apellido" v-model="form.surname"
                                    class="w-full outline-none text-sm bg-transparent" autocomplete="off" />
                            </div>
                        </div>
                        <!-- Género -->
                        <div class="flex flex-col w-full relative gap-1">
                            <label class="font-semibold text-sm lg:text-base"> Género </label>
                            <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2 relative cursor-pointer"
                                @click="isDropdownOpen = !isDropdownOpen">
                                <span class="material-symbols-rounded text-gray-500 me-2" style="font-size: 1.2rem;">
                                    diversity_3
                                </span>
                                <span class="text-sm lg:text-base select-none">
                                    {{ form.genre || 'Género' }}
                                </span>
                                <span class="material-symbols-rounded absolute right-4 text-gray-500"> expand_more
                                </span>
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

                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <!-- Usuario -->
                    <div class="flex flex-col gap-1">
                        <label class="font-semibold text-sm lg:text-base" for="username"> Usuario </label>
                        <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-3 py-2">
                            <span class="material-symbols-rounded text-gray-500 me-2 text-lg"> account_circle
                            </span>
                            <input id="username" type="text" placeholder="user123" v-model="form.username"
                                class="w-full outline-none text-sm bg-transparent" autocomplete="off" />
                        </div>
                    </div>
                    <!-- Contraseña -->
                    <div class="flex flex-col gap-1">
                        <label class="font-semibold text-sm lg:text-base" for="password"> Contraseña </label>
                        <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-3 py-2">
                            <span class="material-symbols-rounded text-gray-500 me-2 text-lg"> password </span>
                            <input id="password" type="password" placeholder="********" v-model="form.password"
                                class="w-full outline-none text-sm bg-transparent" autocomplete="off" />
                        </div>
                    </div>
                </div>
            </form>
            <div v-if="isLoading" class="flex justify-center mt-4">
                <div class="loader"></div>
            </div>
        </NeoModal>
    </div>
</template>
