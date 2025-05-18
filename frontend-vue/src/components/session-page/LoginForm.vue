<script setup>
import { onMounted, ref } from 'vue';
import NeoButton from '../NeoButton.vue';
import { useToast } from 'vue-toastification';
import { useRouter } from 'vue-router';
import { useAuth } from '../../composables/useAuth';

const toast = useToast()
const router = useRouter()
const { login, fetchUser, isLogged, userData } = useAuth()

const form = ref({
    username: '',
    password: '',
});

const fetchLogin = async () => {
    const response = await login(form.value);

    if (response?.data?.message) {
        toast.success("Bienvenido " + response.data.user + "!", {
            toastClassName: "my-custom-toast-class",
        });

        const res = await fetchUser(); 
        console.log(res); 

        if (res.role === "mentor") {
            router.push(`/home/mentor/${res.data.user_id}`);
        } else if (res.role === "student") {
            router.push(`/home/student/${res.data.user_id}`);
        } else {
            router.push('/error');
        }
    } else {
        toast.error("Error al iniciar sesión", {
            toastClassName: "my-custom-toast-class",
        });
    }
};

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
