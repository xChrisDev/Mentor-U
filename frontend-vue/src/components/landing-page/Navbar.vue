<script setup>
import { useRouter } from 'vue-router';
import NeoButton from '../NeoButton.vue';
import NeoContainer from '../NeoContainer.vue';


const router = useRouter()
</script>

<template>
    <div class="w-full">
        <nav class="flex justify-between items-center py-6 gap-4">
            <NeoContainer class="flex items-center gap-4" bg="bg-[#96FEAD]">
                <img src="/favicon.png" class="h-12" alt="favicon">
            </NeoContainer>

            <NeoContainer class="flex gap-8" bg="bg-[#EBDFFF]">
                <a class="font-ppgosha font-normal text-lg rounded-lg px-2 hover:bg-[#D8C0FF] transition-all"
                    href="#">Home</a>
                <a class="font-ppgosha font-normal text-lg rounded-lg px-2 hover:bg-[#D8C0FF] transition-all"
                    href="#">Code</a>
                <a class="font-ppgosha font-normal text-lg rounded-lg px-2 hover:bg-[#D8C0FF] transition-all"
                    href="#">About Us</a>
            </NeoContainer>

            <NeoButton text="Ingresar" icon="input" bg="#96FEAD" @click="router.push('/login')"/>
        </nav>
    </div>
</template>