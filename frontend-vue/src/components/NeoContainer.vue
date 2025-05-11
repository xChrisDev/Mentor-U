<script setup>
const props = defineProps({
    bg: String
})
</script>

<template>
    <div :class="['flex text-black border-2 border-black p-2 rounded-lg transition-all font-semibold shadow-[4px_4px_0px_0px_black]', bg]">
        <slot />
    </div>
</template>
