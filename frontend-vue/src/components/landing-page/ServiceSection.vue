<script setup>
import ServiceCard from './ServiceCard.vue';
</script>

<template>
    <section id="services" class="mt-32 mb-18">
        <h1 class="text-center font-bold text-5xl mb-12">Eleva tu conocimiento e impulsa tus habilidades</h1>
        <div class="grid grid-cols-2 gap-10">
            <ServiceCard title="Programación"
                description="Aprende programación desde cero, hasta convertirte en un experto en cualquier tecnologia que desees."
                icon="code" img="./img/programming.webp" />
            <ServiceCard title="Creatividad"
                description="Impulsa tu creatividad desarrollando proyectos que permitan expresar tu visión."
                icon="draw" img="./img/creative.webp" />
            <ServiceCard title="Chat"
                description="Chatea con todos tus mentores en tiempo real para resolver tus dudas y continuar tu aprendizaje."
                icon="chat" img="./img/chat.webp" />
            <ServiceCard title="Recursos"
                description="Consulta los recursos gratuitos de nuestros mentores y comparte los tuyos para ayudar a los demás."
                icon="collections_bookmark" img="./img/resources.webp" />
        </div>
    </section>
</template>
