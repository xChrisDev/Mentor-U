<script setup>
import { ref } from 'vue';
import NeoButton from '../NeoButton.vue';
import NeoModal from '../NeoModal.vue';
import { postProblem } from '../../services/problemService';
import { useToast } from 'vue-toastification';

const props = defineProps({
    id_mentor: Number,
    id_mentorie: Number
});
const emit = defineEmits(['update'])
const toast = useToast();
const modalRef = ref(null);
const form = ref({
    topic: '',
    level: '',
    lang: ''
});

const isDropdownOpen = ref(false);
const levelOptions = ['Fácil', 'Media', 'Difícil'];
const isLoading = ref(false);

function selectLevel(option) {
    form.value.level = option;
    isDropdownOpen.value = false;
}

const openModal = () => {
    modalRef.value?.open();
};

const handleConfirm = async () => {
    isLoading.value = true;
    let level = "";
    if (form.value.level === 'Fácil') level = 'facil';
    else if (form.value.level === 'Media') level = 'media';
    else if (form.value.level === 'Difícil') level = 'dificil';

    const data = {
        topic: form.value.topic,
        level: level,
        lang: form.value.lang,
        id_mentor: props.id_mentor,
        id_mentorie: props.id_mentorie
    };

    try {
        const response = await postProblem(data);
        console.log(response);

        if (response.problem) {
            toast.success(response.message, {
                toastClassName: "my-custom-toast-class",
            });
            emit('update')
            modalRef.value?.close();
            isLoading.value = false;
        } else {
            toast.error(response.message, {
                toastClassName: "my-custom-toast-class",
            });
            isLoading.value = false;
        }
    } catch (error) {
        toast.error("Ocurrió un error al generar el problema.", {
            toastClassName: "my-custom-toast-class",
        });
        isLoading.value = false;
    } finally {
        isLoading.value = false;
    }
};
</script>

<template>
    <div>
        <NeoButton bg="#96FEAD" icon="add_circle" text="Nuevo" @click="openModal" />

        <NeoModal ref="modalRef" title="Nuevo problema" icon="psychology_alt" @confirm="handleConfirm">
            <form class="flex flex-col gap-4">
                <div class="flex flex-col gap-2">
                    <!-- Tópico -->
                    <div class="flex flex-col gap-1 w-full">
                        <label class="font-semibold text-sm lg:text-base" for="topic"> Tópico </label>
                        <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2">
                            <span class="material-symbols-rounded text-gray-500 me-2"> label </span>
                            <input id="topic" type="text" placeholder="Estructuras de datos" v-model="form.topic"
                                class="w-full outline-none text-sm lg:text-base bg-transparent" autocomplete="off" />
                        </div>
                    </div>

                    <!-- Dificultad -->
                    <div class="flex flex-col gap-1 w-full relative">
                        <label class="font-semibold text-sm lg:text-base"> Dificultad </label>
                        <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2 relative cursor-pointer"
                            @click="isDropdownOpen = !isDropdownOpen">
                            <span class="material-symbols-rounded text-gray-500 me-2" style="font-size: 1.2rem;"> speed
                            </span>
                            <span class="text-sm lg:text-base select-none">
                                {{ form.level || 'Selecciona una opción' }}
                            </span>
                            <span class="material-symbols-rounded absolute right-4 text-gray-500"> expand_more </span>
                        </div>

                        <!-- Opciones -->
                        <div v-show="isDropdownOpen"
                            class="absolute top-full mt-2 left-0 right-0 border-[3px] border-black rounded-xl bg-white z-50">
                            <div v-for="option in levelOptions" :key="option" @click="selectLevel(option)"
                                class="px-4 py-2 rounded-xl cursor-pointer hover:bg-gray-200 text-sm lg:text-base">
                                {{ option }}
                            </div>
                        </div>
                    </div>

                    <!-- Lenguaje -->
                    <div class="flex flex-col gap-1 w-full">
                        <label class="font-semibold text-sm lg:text-base" for="lang"> Lenguaje </label>
                        <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2">
                            <span class="material-symbols-rounded text-gray-500 me-2"> code </span>
                            <input id="lang" type="text" placeholder="Python, JavaScript..." v-model="form.lang"
                                class="w-full outline-none text-sm lg:text-base bg-transparent" autocomplete="off" />
                        </div>
                    </div>
                </div>
            </form>
            
            <div v-if="isLoading" class="flex justify-center mt-4">
                <div class="loader" data-aos="zoom-in" data-aos-delay="100"></div>
            </div>
        </NeoModal>
    </div>
</template>
