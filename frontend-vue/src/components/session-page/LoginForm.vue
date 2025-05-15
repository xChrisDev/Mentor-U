<script setup>
import { ref } from 'vue';
import NeoButton from '../NeoButton.vue';
import { loginUser, getUserData } from '../../services/userService.js'
import { useToast } from 'vue-toastification';
import { useRouter } from 'vue-router';

const toast = useToast()
const router = useRouter()

const form = ref({
    username: '',
    password: '',
});

const fetchLogin = async () => {
    const response = await loginUser(form.value);
    if (response.detail) {
        toast.error(detail, {
            toastClassName: "my-custom-toast-class",
        });
    }

    if (response.access_token) {
        toast.success("Inicio de sesión autorizado", {
            toastClassName: "my-custom-toast-class",
        });

        const data = await getUserData(form.value.username)
        console.log(data)
        if (data.role == "mentor") {
            router.push('/home/mentor')
        } else if (data.role == "student") {
            router.push('/home/student')
        } else {
            router.push('/error')
        }
    }
}

</script>

<template>
    <form class="flex flex-col gap-4">
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
        <NeoButton text="Entrar" icon="login" bg="#96FEAD" class="mt-4 justify-center" @click="fetchLogin" />
    </form>
</template>
