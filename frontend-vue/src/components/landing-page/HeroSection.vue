<script setup>
import { Button } from 'primevue';
</script>

<template>
    <section id="home" class="flex items-center justify-between gap-12 md:gap-20 mt-42 h-[70dvh]">
        <article class="space-y-4 text-center md:text-left">
            <h1 class="flex gap-4 font-bold text-6xl text-[var(--light-green-icon)]">
                Mentor-U
                <span class="material-symbols-rounded" style="font-size: 4rem;">
                    school
                </span>
            </h1>
            <h2 class="font-bold text-3xl md:text-5xl">Desbloquea tu máximo potencial.</h2>
            <p class="text-lg md:text-xl">
                Conviértete en un experto en el tema que prefieras, aprende de los mejores.
            </p>
            <Button rounded class="items-center gap-2 px-6 py-3 text-lg font-semibold mt-8">
                Empezar
                <span class="material-symbols-rounded">arrow_outward</span>
            </Button>
        </article>

        <article class="flex flex-col items-center">
            <div class="bg-[var(--light-green-icon)] rounded-3xl p-2 shadow-lg">
                <canvas class="rounded-2xl" id="canvas" width="400" height="400"></canvas>
            </div>

            <div class="grid grid-cols-3 text-center mt-6 w-full max-w-sm">
                <div>
                    <p class="text-3xl md:text-4xl text-[var(--light-green-icon)] font-bold">2+</p>
                    <p class="text-base md:text-lg">Años</p>
                </div>
                <div>
                    <p class="text-3xl md:text-4xl text-[var(--light-green-icon)] font-bold">90+</p>
                    <p class="text-base md:text-lg">Mentores</p>
                </div>
                <div>
                    <p class="text-3xl md:text-4xl text-[var(--light-green-icon)] font-bold">300+</p>
                    <p class="text-base md:text-lg">Asesorías</p>
                </div>
            </div>
        </article>
    </section>

</template>
