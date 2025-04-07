<script setup>
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';
</script>

<template>
    <div class="flex justify-center">
        <div class="w-[80%]">
            <Navbar />
            <slot />
            <Footer />
        </div>
    </div>
</template>
