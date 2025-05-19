<script setup>
const emit = defineEmits(['click'])

const props = defineProps({
  icon: String,
  text: String,
  bg: String,
  type: {
    type: String,
    default: 'button',
  },
})

const hoverBg = props.bg + 'CC'
</script>

<template>
  <button
    :type="type"
    class="cursor-pointer flex items-center justify-center text-black border-2 border-black p-2 rounded-lg transition-all font-semibold shadow-[4px_4px_0px_0px_black] hover:shadow-none hover:scale-[101%]"
    :style="{ backgroundColor: bg, '--hover-bg': hoverBg }"
    @click="emit('click')"
    @mouseover="($event.currentTarget.style.backgroundColor = hoverBg)"
    @mouseleave="($event.currentTarget.style.backgroundColor = bg)"
  >
    <span v-if="text" class="mr-2">{{ text }}</span>
    <span v-if="icon" class="material-symbols-rounded">{{ icon }}</span>
  </button>
</template>
