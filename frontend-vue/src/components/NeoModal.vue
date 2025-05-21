<script setup>
import { ref } from 'vue';
import NeoButton from './NeoButton.vue';

const props = defineProps({
    title: {
        type: String,
        default: 'Modal'
    },
    icon: {
        type: String,
        default: 'add'
    },
    bg: {
        type: String,
        default: '#96FEAD'
    }
});

const emit = defineEmits(['confirm']);

const modal = ref(null);
const isOpen = ref(false);
const isClosing = ref(false);

const open = () => {
    isOpen.value = true;
    isClosing.value = false;
    modal.value?.showModal();
};

const close = () => {
    isClosing.value = true;

    setTimeout(() => {
        isOpen.value = false;
        modal.value?.close();
        isClosing.value = false;
    }, 300);
};

defineExpose({
    open,
    close
});
</script>

<template>
    <div v-if="isOpen"
        class="fixed inset-0 z-40 w-full h-screen bg-black/60 backdrop-blur-sm transition-opacity duration-300"
        :class="{ 'opacity-100': !isClosing, 'opacity-0': isClosing }" style="left: 0; right: 0; margin: 0;"
        @click.self="close"></div>


    <dialog ref="modal" class="open:fixed open:top-1/2 open:left-1/2 open:-translate-x-1/2 open:-translate-y-1/2
    border-4 border-black rounded-xl w-xl p-4 bg-white shadow-[4px_4px_0px_0px_black]
    z-50 transition-all duration-300" :class="{
        'animate-scale-in': !isClosing,
        'animate-scale-out': isClosing
    }">

        <div class="flex items-center justify-center gap-2 mb-4 bg-[] p-1 border-3 rounded-lg" :style="{ backgroundColor: bg }">
            <span v-if="icon" class="material-symbols-rounded" style="font-size: 2rem;">{{ icon }}</span>
            <h2 class="text-2xl font-bold">{{ title }}</h2>
        </div>

        <div class="mb-6">
            <slot />
        </div>

        <div class="grid grid-cols-2 justify-center gap-2">
            <NeoButton icon="check" bg="#96FEAD" @click="$emit('confirm')" />
            <NeoButton icon="close" bg="#FFADAD" @click="close" />
        </div>
    </dialog>
</template>

<style scoped>
@keyframes scale-in {
    0% {
        opacity: 0;
        transform: scale(0.8);
    }

    100% {
        opacity: 1;
        transform: scale(1);
    }
}

@keyframes scale-out {
    0% {
        opacity: 1;
        transform: scale(1);
    }

    100% {
        opacity: 0;
        transform: scale(0.8);
    }
}

.animate-scale-in {
    animation: scale-in 0.3s ease forwards;
}

.animate-scale-out {
    animation: scale-out 0.3s ease forwards;
}
</style>