<script setup>
import { Button } from 'primevue';

defineProps({
    title: {
        type: String,
        required: true
    },
    description: {
        type: String,
        required: true
    },
    icon: {
        type: String,
        required: true
    },
    img: {
        type: String,
    }
});
</script>

<template>
    <article
        class="rounded-3xl p-6 flex flex-col gap-6 bg-gray-500/10 backdrop-blur-lg duration-300 w-full">

        <img v-if="img" :src="img" alt="Imagen del servicio" class="w-full h-64 object-cover rounded-2xl mb-2" />

        <div class="flex gap-6">
            <div>
                <div class="bg-[var(--light-green-icon)] text-white rounded-2xl p-4 flex justify-center items-center">
                    <span class="material-symbols-rounded" style="font-size: 2rem;">{{ icon }}</span>
                </div>
            </div>
            <div class="space-y-3">
                <h2 class="font-bold text-3xl ">{{ title }}</h2>
                <p class="text-lg leading-relaxed">
                    {{ description }}
                </p>
            </div>
        </div>
    </article>
</template>
