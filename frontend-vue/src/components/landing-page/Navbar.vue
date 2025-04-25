<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { Button } from 'primevue';

const navIsScrolled = ref(false);
const activeOption = ref('home');

// Detectar la sección visible y resaltar el enlace correspondiente
const sections = ref([]);
const handleScroll = () => {
    navIsScrolled.value = window.scrollY > 20;

    // Verificar cuál sección está visible y activar el enlace correspondiente
    sections.value.forEach((section) => {
        const sectionRect = section.getBoundingClientRect();
        if (sectionRect.top <= 0 && sectionRect.bottom >= 0) {
            activeOption.value = section.id;
        }
    });
};

onMounted(() => {
    // Almacenar las secciones para hacer el cálculo
    sections.value = document.querySelectorAll('section');
    window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll);
});

const setOption = (option) => {
    activeOption.value = option;
};

const toggleDarkMode = () => {
    document.documentElement.classList.toggle('my-app-dark');
};

const scrollToSection = (sectionId) => {
    const section = document.getElementById(sectionId);
    section.scrollIntoView({ behavior: 'smooth' });
};
</script>

<template>
    <nav :class="[
        'fixed top-0 left-1/2 transform -translate-x-1/2 z-50 flex justify-between items-center gap-2 p-4 transition duration-300 rounded-3xl w-[80%] mt-4',
        navIsScrolled ? 'bg-white/10 shadow-md backdrop-blur' : 'bg-transparent'
    ]">
        <img src="/favicon.png" alt="favicon" class="w-16 h-16 bg-[var(--light-green-icon)] p-2 rounded-xl" />

        <ul class="flex gap-8 items-center">
            <li>
                <a href="#home" @click="scrollToSection('home'); setOption('home')" :class="[
                    'font-semibold px-6 py-3 rounded-3xl transition-colors duration-200 cursor-pointer shadow-md',
                    activeOption === 'home' ? 'bg-[var(--light-green-icon)] text-white' : 'bg-gray-100 hover:bg-[var(--light-green-icon)] text-black hover:text-white'
                ]">
                    Home
                </a>
            </li>
            <li>
                <a href="#services" @click="scrollToSection('services'); setOption('services')" :class="[
                    'font-semibold px-6 py-3 rounded-3xl transition-colors duration-200 cursor-pointer shadow-md',
                    activeOption === 'services' ? 'bg-[var(--light-green-icon)] text-white' : 'bg-gray-100 hover:bg-[var(--light-green-icon)] text-black hover:text-white'
                ]">
                    Services
                </a>
            </li>
            <li>
                <a href="#about" @click="scrollToSection('about'); setOption('about')" :class="[
                    'font-semibold px-6 py-3 rounded-3xl transition-colors duration-200 cursor-pointer shadow-md',
                    activeOption === 'about' ? 'bg-[var(--light-green-icon)] text-white' : 'bg-gray-100 hover:bg-[var(--light-green-icon)] text-black hover:text-white'
                ]">
                    About
                </a>
            </li>
        </ul>

        <Button @click="toggleDarkMode()" severity="contrast" rounded class="w-12 h-12">
            <span class="material-symbols-rounded"> dark_mode </span>
        </Button>
    </nav>
</template>
