<script setup>
const props = defineProps({
    icon: String,
    text: String,
    bg: String,
})

const hoverBg = props.bg + 'CC'
</script>

<template>
    <button
        class="cursor-pointer flex text-black border-2 border-black p-2 rounded-lg transition-all font-semibold shadow-[4px_4px_0px_0px_black] hover:shadow-none hover:scale-105"
        :style="{
            backgroundColor: bg,
            '--hover-bg': hoverBg
        }" @mouseover="($event.currentTarget.style.backgroundColor = hoverBg)"
        @mouseleave="($event.currentTarget.style.backgroundColor = bg)">
        {{ text }}
        <span class="ms-2 material-symbols-rounded">{{ icon }}</span>
    </button>
</template>
