<script setup>
import { ref } from 'vue';
import NeoButton from '../NeoButton.vue';
import NeoModal from '../NeoModal.vue';
import { putMentorie } from '../../services/mentorieService';
import { useToast } from 'vue-toastification';

const props = defineProps({
    mentorie: Object
})

const emit = defineEmits(['update'])
const toast = useToast();
const modalRef = ref(null);
const isLoading = ref(false);
const form = ref({
    id_mentorie: props.mentorie.id,
    id_mentor: props.mentorie.id_mentor,
    title: props.mentorie.title,
    description: props.mentorie.description,
    price: props.mentorie.price,
    duration: props.mentorie.duration,
    max_students: props.mentorie.max_students,
    file: null,
    preview: props.mentorie.image || null
});

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

const openModal = () => {
    modalRef.value?.open();
};

const handleConfirm = async () => {
    isLoading.value = true
    const formData = new FormData()
    formData.append('id_mentor', form.value.id_mentor)
    formData.append('title', form.value.title)
    formData.append('description', form.value.description)
    formData.append('price', form.value.price)
    formData.append('duration', form.value.duration)
    formData.append('max_students', form.value.max_students)
    if (form.value.file) {
        formData.append('image', form.value.file)
    }


    const response = await putMentorie(form.value.id_mentorie, formData)
    if (response.mentor_id) {
        toast.success(response.message, {
            toastClassName: "my-custom-toast-class",
        });
        emit('update')
        isLoading.value = false
        modalRef.value?.close();
    } else {
        toast.error(response.message, {
            toastClassName: "my-custom-toast-class",
        });
        isLoading.value = false
    }
}

</script>

<template>
    <div>
        <NeoButton bg="#FFF6D1" icon="edit" @click="openModal" />

        <NeoModal ref="modalRef" title="Editar mentoria" icon="menu_book" bg="#FFF6D1" @confirm="handleConfirm">
            <form class="flex flex-col gap-4">
                <div class="flex flex-col gap-2">
                    <div class="flex flex-col gap-1">
                        <label class="font-semibold text-sm lg:text-base"> Portada </label>
                        <div class="flex items-center hover:grayscale transition-all justify-center border-[3px] border-black rounded-xl bg-white w-full h-32 cursor-pointer relative overflow-hidden"
                            @click="triggerFileSelect">
                            <input id="fileInput" type="file" accept="image/*" @change="handleFileChange"
                                class="hidden" />
                            <img v-if="form.preview" :src="form.preview" alt="Preview"
                                class="w-full h-full object-cover" />
                            <span v-else class="material-symbols-rounded text-4xl text-gray-500"> image </span>
                        </div>
                    </div>

                    <div class="grid grid-cols-3 gap-4">
                        <div class="col-span-2">
                            <!-- Titulo -->
                            <div class="flex flex-col gap-1 w-full">
                                <label class="font-semibold text-sm lg:text-base" for="title"> Titulo </label>
                                <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2">
                                    <span class="material-symbols-rounded text-gray-500 me-2"
                                        style="font-size: 1.2rem;">
                                        account_circle </span>
                                    <input id="title" type="text" placeholder="Introducción en python..."
                                        v-model="form.title"
                                        class="w-full outline-none text-sm lg:text-base bg-transparent"
                                        autocomplete="off" />
                                </div>
                            </div>
                            <!-- Descripción -->
                            <div class="flex flex-col gap-1 w-full mt-3">
                                <label class="font-semibold text-sm lg:text-base" for="description"> Descripción
                                </label>
                                <div class="border-[3px] border-black rounded-xl bg-white px-4 py-2">
                                    <textarea id="description" rows="4" placeholder="Cuéntanos sobre tu mentoria..."
                                        v-model="form.description"
                                        class="w-full outline-none text-sm lg:text-base bg-transparent resize-none"></textarea>
                                </div>
                            </div>
                        </div>

                        <div class="flex flex-col gap-2 w-full">
                            <!-- Precio -->
                            <div class="flex flex-col gap-1 w-full">
                                <label class="font-semibold text-sm lg:text-base" for="price"> Precio </label>
                                <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2">
                                    <span class="material-symbols-rounded text-gray-500 me-2"
                                        style="font-size: 1.2rem;">
                                        account_circle </span>
                                    <input id="price" type="number" placeholder="99.99" v-model="form.price"
                                        class="w-full outline-none text-sm lg:text-base bg-transparent"
                                        autocomplete="off" />
                                </div>
                            </div>

                            <!-- Duracion -->
                            <div class="flex flex-col gap-1 w-full">
                                <label class="font-semibold text-sm lg:text-base" for="duration"> Horas de duración
                                </label>
                                <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2">
                                    <span class="material-symbols-rounded text-gray-500 me-2"
                                        style="font-size: 1.2rem;">
                                        account_circle </span>
                                    <input id="duration" type="number" placeholder="8" v-model="form.duration"
                                        class="w-full outline-none text-sm lg:text-base bg-transparent"
                                        autocomplete="off" />
                                </div>
                            </div>

                            <!-- Estudiantes -->
                            <div class="flex flex-col gap-1 w-full">
                                <label class="font-semibold text-sm lg:text-base" for="max_students"> Estudiantes
                                    máximos
                                </label>
                                <div class="flex items-center border-[3px] border-black rounded-xl bg-white px-4 py-2">
                                    <span class="material-symbols-rounded text-gray-500 me-2"
                                        style="font-size: 1.2rem;">
                                        account_circle </span>
                                    <input id="max_students" type="number" placeholder="30" v-model="form.max_students"
                                        class="w-full outline-none text-sm lg:text-base bg-transparent"
                                        autocomplete="off" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div v-if="isLoading" class="flex justify-center mt-4">
                    <div class="loader"></div>
                </div>
            </form>
        </NeoModal>
    </div>
</template>