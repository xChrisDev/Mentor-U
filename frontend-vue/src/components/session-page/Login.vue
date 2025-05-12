<script setup>
import { ref } from 'vue';
import NeoButton from '../NeoButton.vue';

const form = ref({
    username: '',
    password: '',
});

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

        <NeoButton text="Entrar" bg="#96FEAD" icon="login" class="mt-4 justify-center" />
    </form>
</template>
