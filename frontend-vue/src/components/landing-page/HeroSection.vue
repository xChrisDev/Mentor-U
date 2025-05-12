<script setup>
import { useRouter } from 'vue-router';
import NeoButton from '../NeoButton.vue';
import NeoContainer from '../NeoContainer.vue';
import NeoTab from '../NeoTab.vue';

const router = useRouter();
</script>

<template>
  <NeoContainer bg="bg-[#EBDFFF]" class="flex flex-col p-8 mt-15">
    <div>
      <h1 class="flex items-center font-ppgosha lg:text-2xl 2xl:text-3xl">
        <span class="material-symbols-rounded me-2" style="font-size: 2.5rem;">school</span>
        Mentor-U
      </h1>
    </div>
    <div class="flex justify-between">
      <div class="flex flex-col gap-10 justify-center">
        <div>
          <h2 class="font-ppgosha lg:text-4xl 2xl:text-5xl mb-4">Desbloquea tu máximo potencial</h2>
          <p class="lg:text-lg 2xl:text-2xl font-normal font-ppgosha">
            Conviértete en un experto en el lenguaje que prefieras.<br />
            Aprende programación con los mejores y aprende a tu ritmo.
          </p>
          <div class="mt-6">
            <NeoButton text="Comenzar" icon="arrow_forward" bg="#96FEAD" @click="router.push('/login')"/>
          </div>
        </div>
      </div>
      <div class="flex items-center">
        <img src="../../assets/images/developer.png" class="lg:w-80 2xl:w-[450px]" alt="Developer Image" />
      </div>
    </div>
    <div class="flex flex-col gap-4">
                <p class="flex items-center lg:text-sm 2xl:text-xl font-ppgosha"><span class="material-symbols-rounded">
                        star
                    </span>Popular:</p>
                <div class="flex gap-2 items-center">
                    <NeoTab bg="bg-[#D8C0FF]" icon="network_intelligence_update" text="Tareas generadas con IA" />
                    <NeoTab bg="bg-[#D8C0FF]" icon="chat" text="Chat en tiempo real" />
                    <NeoTab bg="bg-[#D8C0FF]" icon="code" text="+8 Lenguajes de programación" />
                </div>
            </div>
  </NeoContainer>
</template>
