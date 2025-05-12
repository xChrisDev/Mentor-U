<script setup>
import { ref } from 'vue';
import NeoButton from '../NeoButton.vue';

const form = ref({
    name: '',
    surname: '',
    genre: '',
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
</script>

<template>
    <form class="flex flex-col gap-4">
        <div class="flex gap-6">
            <div class="flex flex-col gap-1">
                <label class="font-semibold text-sm lg:text-base"> Foto de perfil </label>
                <div class="flex items-center justify-center border-[3px] border-black rounded-xl bg-white w-32 h-32 cursor-pointer relative overflow-hidden"
                    @click="triggerFileSelect">
                    <input id="fileInput" type="file" accept="image/*" @change="handleFileChange" class="hidden" />
                    <img v-if="form.preview" :src="form.preview" alt="Preview" class="w-full h-full object-cover" />
                    <span v-else class="material-symbols-rounded text-4xl text-gray-500"> image </span>
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
        </div>

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
                    class="px-4 py-2 cursor-pointer hover:bg-gray-200 text-sm lg:text-base border-b border-black last:border-none">
                    {{ option }}
                </div>
            </div>
        </div>

        <NeoButton text="Continuar como estudiante" bg="#96FEAD" icon="arrow_forward" class="mt-4 justify-center" />
    </form>
</template>
