<script setup>
import { Button } from 'primevue';
import { setOption } from '../utils/choseOption';

const toggleDarkMode = () => {
    document.documentElement.classList.toggle('my-app-dark');
    document.querySelector("#home-btn").classList.toggle('bg-gray-100');
    document.querySelector("#about-btn").classList.toggle('bg-gray-100');
    document.querySelector("#services-btn").classList.toggle('bg-gray-100');
    document.querySelector("#contact-btn").classList.toggle('bg-gray-100');
}

</script>

<template>
    <nav class="flex justify-between items-center gap-2 py-4">
        <img src="/icon.png" alt="favicon" class="w-20 h-20 bg-green-100 rounded-3xl" />

        <ul class="flex gap-12 items-center">
            <li id="home-btn" @click="setOption('home')"
                class="bg-gray-100 font-semibold hover:text-white hover:bg-[var(--light-green-icon)] px-6 py-3 rounded-3xl transition-colors duration-200 cursor-pointer active">
                <a href="#home">Home</a>
            </li>
            <li id="about-btn" @click="setOption('about')"
                class="bg-gray-100 font-semibold hover:text-white hover:bg-[var(--light-green-icon)] px-6 py-3 rounded-3xl transition-colors duration-200 cursor-pointer">
                <a href="#home">About</a>
            </li>
            <li id="services-btn" @click="setOption('services')"
                class="bg-gray-100 font-semibold hover:text-white hover:bg-[var(--light-green-icon)] px-6 py-3 rounded-3xl transition-colors duration-200 cursor-pointer">
                <a href="#home">Services</a>
            </li>
            <li id="contact-btn" @click="setOption('contact')"
                class="bg-gray-100 font-semibold hover:text-white hover:bg-[var(--light-green-icon)] px-6 py-3 rounded-3xl transition-colors duration-200 cursor-pointer">
                <a href="#home">Contact</a>
            </li>
        </ul>

        <Button @click="toggleDarkMode()" severity="secondary" rounded class="w-12 h-12">
            <span class="material-symbols-rounded">
                dark_mode
            </span>
        </Button>

    </nav>
</template>
