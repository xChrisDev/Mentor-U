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
  disabled: {
    type: Boolean,
    default: false
  }
})

const hoverBg = props.bg + 'CC'
</script>

<template>
  <button
    :type="type"
    :disabled="disabled"
    class="flex items-center justify-center shadow-[4px_4px_0px_0px_black] text-black border-2 border-black p-2 rounded-lg transition-all font-semibold"
    :class="[
      disabled
        ? 'bg-gray-300 cursor-not-allowed'
        : 'cursor-pointer hover:shadow-none hover:scale-[101%]'
    ]"
    :style="!disabled ? { backgroundColor: bg, '--hover-bg': hoverBg } : {}"
    @click="!disabled && emit('click')"
    @mouseover="!disabled && ($event.currentTarget.style.backgroundColor = hoverBg)"
    @mouseleave="!disabled && ($event.currentTarget.style.backgroundColor = bg)"
  >
    <span v-if="text" class="mr-2">{{ text }}</span>
    <span v-if="icon" class="material-symbols-rounded">{{ icon }}</span>
  </button>
</template>
