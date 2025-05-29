<script setup>
import NeoContainer from '../NeoContainer.vue';
import NeoTab from '../NeoTab.vue';

const props = defineProps({
    data: Object
})

const {
    student_name,
    student_surname,
    student_photo,
    mentorie_title,
    problem_title,
    problem_description,
    problem_difficulty,
    problem_topic,
    result,
    created_at,
    code
} = props.data

const getDifficultyText = (difficulty) => {
    switch (difficulty) {
        case 'facil': return 'Fácil';
        case 'medio': return 'Medio';
        case 'dificil': return 'Difícil';
        default: return 'Desconocido';
    }
};

const getStatusText = (status) => {
    switch (status) {
        case 'pending':
            return 'Pendiente de revisión'
        case 'accepted':
            return 'Aceptado'
        case 'rejected':
            return 'Devuelto'
    }
}

const getStatusColor = (status) => {
    switch (status) {
        case 'pending':
            return 'bg-gray-200';
        case 'accepted':
            return 'bg-[#96FEAD]';
        case 'rejected':
            return 'bg-[#FFADAD]';
    }
}
</script>

<template>
    <NeoContainer
        bg="shadow-none bg-white p-4 w-full flex flex-col gap-4 hover:scale-[101%] transition-all cursor-pointer">

        <div class="flex justify-between items-center gap-4 flex-wrap">
            <div class="flex gap-4 items-center">
                <img :src="student_photo" :alt="`${student_name} ${student_surname}`"
                    class="w-14 h-14 border-2 border-black rounded-full object-cover" />
                <div>
                    <p class="font-bold leading-4">{{ student_name }} {{ student_surname }}</p>
                    <p class="text-sm text-gray-600 leading-4">{{ mentorie_title }}</p>
                </div>
            </div>

            <div class="flex flex-col items-end gap-2">
                <NeoTab :icon="result === 'Correcto' ? 'check_circle' : 'error'" :text="getStatusText(result)"
                    :bg="getStatusColor(result)" />
                <NeoTab icon="schedule" :text="new Date(created_at).toLocaleDateString()" bg="bg-gray-200" />
            </div>
        </div>

        <div class="flex flex-col gap-2">
            <h2 class="text-lg font-bold">{{ problem_title }}</h2>
            <p class="text-sm text-gray-700 font-medium">{{ problem_description }}</p>
            <div class="flex gap-2 flex-wrap">
                <NeoTab icon="psychology" :text="problem_topic" bg="bg-yellow-200" />
                <NeoTab icon="bolt" :text="getDifficultyText(problem_difficulty)" bg="bg-orange-200" />
            </div>
        </div>

    </NeoContainer>
</template>
