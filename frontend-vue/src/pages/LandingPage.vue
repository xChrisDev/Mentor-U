<script setup>
import DefaultLayout from '../layouts/DefaultLayout.vue';
import HeroSection from '../components/landing-page/HeroSection.vue';
import ServicesSection from '../components/landing-page/ServiceSection.vue';
import AboutSection from '../components/landing-page/AboutSection.vue';

</script>

<template>
    <DefaultLayout>
        <HeroSection />
        <ServicesSection />
        <AboutSection />
    </DefaultLayout>
</template>
