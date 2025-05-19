<script setup>
import { ref } from 'vue';
import NeoButton from '../NeoButton.vue';
import { registerUser } from '../../services/userService';
import { useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';
import { useAuth } from '../../composables/useAuth';

const router = useRouter()
const { setUserData, setJustRegistered } = useAuth()
const toast = useToast()

const form = ref({
    email: '',
    username: '',
    password: '',
    role: ''
});

const isDropdownOpen = ref(false);
const roleOptions = ['Mentor', 'Estudiante'];

function selectOption(option) {
    form.value.role = option;
    isDropdownOpen.value = false;
}

const fetchRegister = async () => {
    let role_selected = ""

    if (form.value.role == "Mentor") {
        role_selected = "mentor"
    } else if (form.value.role = "Estudiante") {
        role_selected = "student"
    }

    const user = {
        email: form.value.email,
        username: form.value.username,
        password: form.value.password,
        role: role_selected
    }

    const res = await registerUser(user);

    if (res.user) {
        setUserData({
            id: res.user,
            email: form.value.email,
            username: form.value.username,
            password: form.value.password,
            role: role_selected
        })
        setJustRegistered(true);
        toast.success(res.message, {
            toastClassName: "my-custom-toast-class",
        });
        router.push("/register")
    } else {
        toast.error(res.message, {
            toastClassName: "my-custom-toast-class",
        });
    }
}
</script>

<template>

    <form class="flex flex-col gap-4">
        <div class="flex flex-col gap-1 w-full">
            <label class="font-semibold text-sm lg:text-base" for="email"> Email </label>
            <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2">
                <span class="material-symbols-rounded text-gray-500 me-2" style="font-size: 1.2rem;">
                    email
                </span>
                <input id="email" type="email" placeholder="ejemplo@correo.com" v-model="form.email"
                    class="w-full outline-none text-sm lg:text-base bg-transparent" autocomplete="off" />
            </div>
        </div>

        <div class="flex flex-col gap-1 w-full">
            <label class="font-semibold text-sm lg:text-base" for="username"> Usuario </label>
            <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2">
                <span class="material-symbols-rounded text-gray-500 me-2" style="font-size: 1.2rem;">
                    account_circle
                </span>
                <input id="username" type="text" placeholder="user123" v-model="form.username"
                    class="w-full outline-none text-sm lg:text-base bg-transparent" autocomplete="off" />
            </div>
        </div>

        <div class="flex flex-col gap-1 w-full">
            <label class="font-semibold text-sm lg:text-base" for="password"> Contraseña
            </label>
            <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2">
                <span class="material-symbols-rounded text-gray-500 me-2" style="font-size: 1.2rem;">
                    password
                </span>
                <input id="password" type="password" placeholder="password123" v-model="form.password"
                    class="w-full outline-none text-sm lg:text-base bg-transparent" autocomplete="off" />
            </div>
        </div>

        <div class="flex flex-col gap-1 w-full relative">
            <label class="font-semibold text-sm lg:text-base"> Tipo de usuario </label>

            <!-- Caja principal -->
            <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2 relative cursor-pointer"
                @click="isDropdownOpen = !isDropdownOpen">
                <span class="material-symbols-rounded text-gray-500 me-2" style="font-size: 1.2rem;">
                    diversity_3 </span>
                <span class="text-sm lg:text-base select-none">
                    {{ form.role || 'Selecciona una opción' }}
                </span>
                <span class="material-symbols-rounded absolute right-4 text-gray-500"> expand_more </span>
            </div>

            <!-- Opciones -->
            <div v-show="isDropdownOpen"
                class="absolute top-full mt-2 left-0 right-0 border-[3px] border-black rounded-xl bg-white z-50">
                <div v-for="option in roleOptions" :key="option" @click="selectOption(option)"
                    class="px-4 py-2 rounded-xl cursor-pointer hover:bg-gray-200 text-sm lg:text-base border-black last:border-none">
                    {{ option }}
                </div>
            </div>
        </div>

        <NeoButton @click="fetchRegister" text="Registrarse" bg="#96FEAD" icon="login" class="mt-4 justify-center" />
    </form>
</template>
