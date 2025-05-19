<script setup>
defineProps({
  mentoria: Object
})
</script>

<template>
  <div
    class="border-2 border-black rounded-md overflow-hidden cursor-pointer bg-white hover:scale-[101%] transition-all flex flex-col">
    <img :src="mentoria.image" alt="Imagen de mentoría" class="w-full h-40 object-cover border-b-2 border-black" />

    <div class="p-4 flex flex-col justify-between flex-1">
      <div>
        <h4 class="font-bold text-lg mb-1">{{ mentoria.title }}</h4>
        <p class="text-sm mb-2 text-gray-800 line-clamp-3">
          {{ mentoria.description }}
        </p>
      </div>

      <div class="mt-auto">
        <div class="flex justify-end gap-2 text-sm mt-2">
          <span class="px-2 py-1 bg-[#D8C0FF] font-semibold border border-black rounded-full">
            Duración: {{ mentoria.duration }} hr
          </span>
          <span class="px-2 py-1 bg-[#96FEAD] font-semibold border border-black rounded-full">
            Estudiantes máx: {{ mentoria.max_students }}
          </span>
        </div>

        <div class="mt-3 text-right">
          <span class="text-md font-bold" :class="mentoria.price > 0 ? '' : 'line-through text-gray-600'">
            ${{ mentoria.price.toFixed(2) }}
          </span>
          <span v-if="mentoria.price === 0" class="ml-2 text-md font-bold text-[#96FEAD]">
            Gratis
          </span>
        </div>
      </div>
    </div>
  </div>
</template>
