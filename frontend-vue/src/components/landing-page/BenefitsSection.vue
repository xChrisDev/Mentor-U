<script setup>
import { useRouter } from 'vue-router';
import NeoButton from '../NeoButton.vue';
import NeoContainer from '../NeoContainer.vue';

const router = useRouter()
</script>
<template>
    <section class="mt-40">
        <article class="flex items-center justify-between">
            <div>
                <h2 class="font-ppgosha font-bold lg:text-4xl 2xl:text-5xl mb-2">Beneficios</h2>
                <p class="lg:text-xl 2xl:text-2xl font-normal font-ppgosha">Mentor-U es tu mejor opción para
                    aprender de forma fácil y rápida.</p>
            </div>
            <NeoButton icon="arrow_forward" text="Explorar" bg="#FDD965" @click="router.push('/login')" />
        </article>
        <article class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
            <NeoContainer bg="bg-[#FFEECE]" class="flex flex-col p-6">
                <div class="bg-[#fce2b4] flex items-center justify-center rounded-lg p-2 w-fit mb-2">
                    <span class="material-symbols-rounded" style="font-size: 5rem;">
                        interests
                    </span>
                </div>
                <h3 class="font-ppgosha font-bold text-2xl 2xl:text-3xl mb-2">Contenido Personalizado</h3>
                <p class="lg:text-base 2xl:text-lg">Aprende a tu ritmo con ejercicios y lecciones ajustadas a tus
                    habilidades y objetivos.</p>
            </NeoContainer>
            <NeoContainer bg="bg-[#FFEECE]" class="flex flex-col p-6">
                <div class="bg-[#fce2b4] flex items-center justify-center rounded-lg p-2 w-fit mb-2">
                    <span class="material-symbols-rounded" style="font-size: 5rem;">
                        network_intelligence
                    </span>
                </div>
                <h3 class="font-ppgosha font-bold text-2xl 2xl:text-3xl mb-2">Asistencia con IA</h3>
                <p class="lg:text-base 2xl:text-lg">Resuelve tus dudas en tiempo real con ayuda de inteligencia
                    artificial integrada.</p>
            </NeoContainer>
            <NeoContainer bg="bg-[#FFEECE]" class="flex flex-col p-6">
                <div class="bg-[#fce2b4] flex items-center justify-center rounded-lg p-2 w-fit mb-2">
                    <span class="material-symbols-rounded" style="font-size: 5rem;">
                        code_blocks
                    </span>
                </div>
                <h3 class="font-ppgosha font-bold text-2xl 2xl:text-3xl mb-2">Amplia variedad de lenguajes</h3>
                <p class="lg:text-base 2xl:text-lg">Desde Python hasta Rust, aprende el lenguaje que mejor se adapte
                    a tu meta profesional.</p>
            </NeoContainer>
            <NeoContainer bg="bg-[#FFEECE]" class="flex flex-col p-6">
                <div class="bg-[#fce2b4] flex items-center justify-center rounded-lg p-2 w-fit mb-2">
                    <span class="material-symbols-rounded" style="font-size: 5rem;">
                        groups
                    </span>
                </div>
                <h3 class="font-ppgosha font-bold text-2xl 2xl:text-3xl mb-2">Comunidad activa</h3>
                <p class="lg:text-base 2xl:text-lg">Únete a una comunidad de estudiantes, mentores y desarrolladores
                    con intereses afines.</p>
            </NeoContainer>
        </article>
    </section>
</template>
