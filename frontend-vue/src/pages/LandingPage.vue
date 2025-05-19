<script setup>
import AboutSection from '../components/landing-page/AboutSection.vue';
import BenefitsSection from '../components/landing-page/BenefitsSection.vue';
import FooterSection from '../components/landing-page/FooterSection.vue';
import HeroSection from '../components/landing-page/HeroSection.vue';
import Navbar from '../components/landing-page/Navbar.vue';
import OpinionSection from '../components/landing-page/OpinionSection.vue';
import TechSection from '../components/landing-page/TechSection.vue';

</script>

<template>
    <div class="relative contianer mx-auto w-[75%]" data-aos="zoom-in" data-aos-delay="100">
        <Navbar />
        <HeroSection data-aos="fade-up" data-aos-delay="300" />
        <BenefitsSection data-aos="fade-up" data-aos-delay="300" />
        <AboutSection data-aos="fade-up" data-aos-delay="300" />
        <TechSection data-aos="fade-up" data-aos-delay="300" />
        <OpinionSection data-aos="fade-up" data-aos-delay="300" />
        <FooterSection data-aos="fade-up" data-aos-delay="300" />
    </div>
</template>
