<script setup>
import { ref } from 'vue';
import NeoButton from '../NeoButton.vue';
import NeoModal from '../NeoModal.vue';
import { deleteMentorie } from '../../services/mentorieService';
import { useToast } from 'vue-toastification';

const props = defineProps({
    mentorie: Object
})

const emit = defineEmits(['delete'])
const toast = useToast();
const modalRef = ref(null);
const isLoading = ref(false);

const openModal = () => {
    modalRef.value?.open();
};

const handleConfirm = async () => {
    isLoading.value = true
    const response = await deleteMentorie(props.mentorie.id)
    toast.success(response.message, {
        toastClassName: "my-custom-toast-class",
    });
    emit('delete')
    isLoading.value = false
    modalRef.value?.close();
}

</script>

<template>
    <div>
        <NeoButton bg="#FFADAD" icon="delete" @click="openModal" />

        <NeoModal ref="modalRef" title="Eliminar mentoria" icon="menu_book" bg="#FFADAD" @confirm="handleConfirm">
            <div class="flex justify-center">
                <p class="text-xl font-medium">¿Estás seguro de eliminar la mentoria?</p>
            </div>
        </NeoModal>
    </div>
</template>