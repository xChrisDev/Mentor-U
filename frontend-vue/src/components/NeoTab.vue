<script setup>
const props = defineProps({
    icon: String,
    text: String,
    bg: String
})
</script>

<template>
    <div :class="['font-medium flex border-2 border-black rounded-2xl py-1 px-2 items-center justify-center shadow-[1px_1px_0px_0px_black]', bg]">
        <span class=" me-1 material-symbols-rounded">{{ icon }}</span>
        <p class="lg:text-sm 2xl:text-md">{{ text }}</p>
    </div>
</template>