<script setup>
import NeoButton from '../components/NeoButton.vue';
import NeoContainer from '../components/NeoContainer.vue';
import NeoNavbar from '../components/NeoNavbar.vue';
import NeoTab from '../components/NeoTab.vue';
</script>

<template>
    <div class="relative">
        <NeoNavbar />
        <NeoContainer bg="bg-[#EBDFFF]" class="flex flex-col p-8 mt-10">
            <div>
                <h1 class="flex items-center font-ppgosha lg:text-2xl 2xl:text-3xl"><span
                        class="material-symbols-rounded me-2" style="font-size: 2.5rem;">
                        school
                    </span>Mentor-U</h1>
            </div>
            <div class="flex justify-between">
                <div class="flex flex-col gap-10 justify-center">
                    <div>
                        <h2 class="font-ppgosha lg:text-4xl 2xl:text-5xl mb-4">Desbloquea tu máximo potencial</h2>
                        <p class="lg:text-lg 2xl:text-2xl font-normal font-ppgosha">
                            Conviértete en un experto en el lenguaje que prefieras.<br /> Aprende programación con los
                            mejores y aprende a tu ritmo.</p>
                        <div class="mt-6">
                            <NeoButton text="Comenzar" icon="arrow_forward" bg="#96FEAD" />
                        </div>
                    </div>
                </div>
                <div class="flex items-center">
                    <img src="../assets/images/developer.png" class="lg:w-80 2xl:w-[450px]" alt="Developer Image" />
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

        <section class="mt-20">
            <article class="flex items-center justify-between">
                <div>
                    <h2 class="font-ppgosha font-bold lg:text-4xl 2xl:text-5xl mb-2">Todas las tecnologías</h2>
                    <p class="lg:text-xl 2xl:text-2xl font-normal font-ppgosha">Descubre los fundamentos y conceptos
                        avanzados de tu tecnología favorita.</p>
                </div>
                <NeoButton icon="arrow_forward" text="Explorar" bg="#FDD965" />
            </article>
            <article class="flex gap-3 flex-wrap justify-center mt-6 px-8">
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

        <section class="mt-20">
            <article class="flex items-center justify-between">
                <div>
                    <h2 class="font-ppgosha font-bold lg:text-4xl 2xl:text-5xl mb-2">Beneficios</h2>
                    <p class="lg:text-xl 2xl:text-2xl font-normal font-ppgosha">Mentor-U es tu mejor opción para
                        aprender de forma fácil y rápida.</p>
                </div>
                <NeoButton icon="arrow_forward" text="Explorar" bg="#FDD965" />
            </article>
            <article class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
                <NeoContainer bg="bg-[#EBDFFF]" class="flex flex-col p-6">
                    <div class="bg-[#F1E9FF] flex items-center justify-center rounded-lg p-2 w-fit mb-2">
                        <span class="material-symbols-rounded" style="font-size: 5rem;">
                            interests
                        </span>
                    </div>
                    <h3 class="font-ppgosha font-bold text-2xl 2xl:text-3xl mb-2">Contenido Personalizado</h3>
                    <p class="lg:text-base 2xl:text-lg">Aprende a tu ritmo con ejercicios y lecciones ajustadas a tus
                        habilidades y objetivos.</p>
                </NeoContainer>
                <NeoContainer bg="bg-[#EBDFFF]" class="flex flex-col p-6">
                    <div class="bg-[#F1E9FF] flex items-center justify-center rounded-lg p-2 w-fit mb-2">
                        <span class="material-symbols-rounded" style="font-size: 5rem;">
                            network_intelligence
                        </span>
                    </div>
                    <h3 class="font-ppgosha font-bold text-2xl 2xl:text-3xl mb-2">Asistencia con IA</h3>
                    <p class="lg:text-base 2xl:text-lg">Resuelve tus dudas en tiempo real con ayuda de inteligencia
                        artificial integrada.</p>
                </NeoContainer>
                <NeoContainer bg="bg-[#EBDFFF]" class="flex flex-col p-6">
                    <div class="bg-[#F1E9FF] flex items-center justify-center rounded-lg p-2 w-fit mb-2">
                        <span class="material-symbols-rounded" style="font-size: 5rem;">
                            code_blocks
                        </span>
                    </div>
                    <h3 class="font-ppgosha font-bold text-2xl 2xl:text-3xl mb-2">Amplia variedad de lenguajes</h3>
                    <p class="lg:text-base 2xl:text-lg">Desde Python hasta Rust, aprende el lenguaje que mejor se adapte
                        a tu meta profesional.</p>
                </NeoContainer>
                <NeoContainer bg="bg-[#EBDFFF]" class="flex flex-col p-6">
                    <div class="bg-[#F1E9FF] flex items-center justify-center rounded-lg p-2 w-fit mb-2">
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
    </div>
</template>
