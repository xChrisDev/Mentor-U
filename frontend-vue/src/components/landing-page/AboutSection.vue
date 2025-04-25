<script setup>
const features = [
    {
        icon: "groups",
        text: "Conecta con mentores expertos en diversas áreas."
    },
    {
        icon: "school",
        text: "Accede a recursos personalizados para tu aprendizaje."
    },
    {
        icon: "chat",
        text: "Participa en conversaciones en tiempo real."
    }
];
</script>

<template>
    <section id="about" class="mb-24">
        <h1 class="font-bold text-5xl text-center mb-16 mt-32">¿Quiénes somos?</h1>

        <div class="px-6 py-10 bg-gray-500/10 backdrop-blur-lg rounded-3xl shadow-xl">
            <img src="../../../public/img/about-us.webp" alt="Imagen ¿Quiénes somos?"
                class="w-full h-64 md:h-96 object-cover rounded-2xl shadow-md mb-10" />

            <p class="text-xl md:text-2xl leading-relaxed text-center mb-12">
                <span class="text-[var(--light-green-icon)] font-bold">Mentor-U</span> es una plataforma diseñada para
                conectar a personas con deseos de aprender programación con mentores expertos.
                Nuestro objetivo es fomentar el aprendizaje y el crecimiento personal a través de experiencias
                personalizadas,
                transmitiendo el conocimiento en sesiones de asesoría y recursos adaptados a tus necesidades.
            </p>

            <ul class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <li v-for="(feature, index) in features" :key="index"
                    class="flex flex-col items-center text-center gap-4 p-6 bg-white/5 backdrop-blur rounded-3xl transition duration-300">
                    <span class="material-symbols-rounded text-white bg-[var(--light-green-icon)] p-4 rounded-2xl"
                        style="font-size: 2rem;">
                        {{ feature.icon }}
                    </span>
                    <p class=" text-lg font-medium">
                        {{ feature.text }}
                    </p>
                </li>
            </ul>
        </div>
    </section>
</template>
