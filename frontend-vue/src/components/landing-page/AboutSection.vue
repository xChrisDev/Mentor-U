<script setup>
import NeoButton from '../NeoButton.vue';
import NeoContainer from '../NeoContainer.vue';

</script>


<template>
    <section class="mt-20">
        <NeoContainer bg="bg-[#EBDFFF]" class="p-8 rounded-2xl">
            <div class="flex flex-col md:flex-row items-center justify-between gap-6">
                <img src="../../assets/images/developer.png" alt="Equipo Mentor-U" class="w-full md:w-1/3 rounded-xl"
                    data-aos="zoom-in" data-aos-delay="200" />

                <div class="flex flex-col gap-4 md:w-1/2" data-aos="fade-left">
                    <h2 class="font-ppgosha text-3xl 2xl:text-5xl font-bold">Sobre Nosotros</h2>
                    <p class="font-normal text-lg 2xl:text-xl">
                        En <strong>Mentor-U</strong> creemos en el poder del aprendizaje colaborativo.
                        Nuestra misión es conectar a estudiantes y mentores para que compartan conocimiento y crezcan
                        juntos.
                    </p>
                    <p class="font-normal text-lg 2xl:text-xl">
                        Somos un equipo de desarrolladores, educadores y entusiastas de la tecnología comprometidos con
                        transformar la forma en que se enseña programación.
                    </p>
                    <div>
                        <NeoButton text="Conoce al equipo" icon="groups" bg="#96FEAD" />
                    </div>
                </div>
            </div>
        </NeoContainer>
    </section>
</template>