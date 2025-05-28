<template>
  <div
    ref="containerRef"
    class="w-full border-2 border-black bg-[#F0F0F0] rounded-lg shadow-[4px_4px_0_0_rgba(0,0,0,1)]"
    style="height: 350px; overflow: hidden;"
  ></div>
</template>

<script setup>
import { onMounted, onBeforeUnmount, ref, watch } from 'vue';
import loader from '@monaco-editor/loader';

const props = defineProps({
  modelValue: String,
  language: {
    type: String,
    default: 'javascript'
  }
});

const emit = defineEmits(['update:modelValue']);
const containerRef = ref(null);
let editor = null;

onMounted(async () => {
  const monaco = await loader.init();

  editor = monaco.editor.create(containerRef.value, {
    value: props.modelValue,
    language: props.language,
    theme: 'vs-dark',
    fontSize: 14,
    minimap: { enabled: false },
    scrollBeyondLastLine: false,
    wordWrap: 'on',
    roundedSelection: false,
    automaticLayout: true,
    lineNumbersMinChars: 3,
  });

  editor.onDidChangeModelContent(() => {
    emit('update:modelValue', editor.getValue());
  });
});

onBeforeUnmount(() => {
  if (editor) {
    editor.dispose();
  }
});

watch(() => props.modelValue, (newVal) => {
  if (editor && editor.getValue() !== newVal) {
    editor.setValue(newVal);
  }
});
</script>

<style scoped>
/* Estilo de scrollbar para reforzar el diseño neobrutalista */
::-webkit-scrollbar {
  width: 10px;
  height: 10px;
}
::-webkit-scrollbar-thumb {
  background: black;
  border: 2px solid white;
}
::-webkit-scrollbar-track {
  background: #f0f0f0;
  border-left: 2px solid black;
}
</style>
