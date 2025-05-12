<script setup>
import { useRouter } from 'vue-router';
import NeoButton from '../NeoButton.vue';
import NeoTab from '../NeoTab.vue';

const router = useRouter()
</script>

<template>
  <section class="mt-40">
    <article class="flex items-center justify-between">
      <div>
        <h2 class="font-ppgosha font-bold lg:text-4xl 2xl:text-5xl mb-2">Todas las tecnologías</h2>
        <p class="lg:text-xl 2xl:text-2xl font-normal font-ppgosha">Descubre los fundamentos y conceptos
          avanzados de tu tecnología favorita.</p>
      </div>
      <NeoButton icon="arrow_forward" text="Explorar" bg="#FDD965" @click="router.push('/login')" />
    </article>
    <article class="flex gap-3 flex-wrap justify-center mt-6 px-16">
      <NeoTab bg="bg-[#FFEECE]" icon="code" text="Java" />
      <NeoTab bg="bg-[#FFEECE]" icon="code" text="Python" />
      <NeoTab bg="bg-[#FFEECE]" icon="code" text="JavaScript" />
      <NeoTab bg="bg-[#FFEECE]" icon="code" text="C#" />
      <NeoTab bg="bg-[#FFEECE]" icon="code" text="C++" />
      <NeoTab bg="bg-[#FFEECE]" icon="code" text="Go" />
      <NeoTab bg="bg-[#FFEECE]" icon="code" text="Rust" />
      <NeoTab bg="bg-[#FFEECE]" icon="code" text="Ruby" />
      <NeoTab bg="bg-[#FFEECE]" icon="code" text="PHP" />
      <NeoTab bg="bg-[#FFEECE]" icon="code" text="Swift" />
      <NeoTab bg="bg-[#FFEECE]" icon="code" text="Kotlin" />
      <NeoTab bg="bg-[#FFEECE]" icon="code" text="TypeScript" />
      <NeoTab bg="bg-[#FFEECE]" icon="code" text="HTML" />
      <NeoTab bg="bg-[#FFEECE]" icon="code" text="CSS" />
      <NeoTab bg="bg-[#FFEECE]" icon="code" text="SQL" />
    </article>
  </section>
</template>
