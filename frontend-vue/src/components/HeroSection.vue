<script setup>
import { Button } from 'primevue';
</script>

<template>
    <section class="flex gap-6 mt-6">
        <article class="flex items-center">
            <div class="pe-24">
                <h1 class="font-bold text-6xl">Desbloquea tu maximo potencial.</h1>
                <p class="text-xl font-thin my-10 text-gray-700">Conviértete en un experto en el tema que prefieras,
                    aprende
                    de los mejores.</p>
                <Button rounded style="padding: 0.7rem 1.5rem;">
                    <span class="font-semibold text-lg">Empezar</span>
                    <span class="material-symbols-rounded">
                        arrow_outward
                    </span>
                </Button>
            </div>
        </article>

        <article>
            <div class="flex bg-[var(--light-green-icon)] rounded-3xl p-2">
                <canvas class="rounded-2xl" id="canvas" width="400" height="400"></canvas>
            </div>
            <div class="grid grid-cols-3 text-center mt-4">
                <div class="col-span-1">
                    <p class="text-4xl">2+</p>
                    <p class="text-lg font-thin text-gray-700">Años</p>
                </div>
                <div class="col-span-1">
                    <p class="text-4xl">90+</p>
                    <p class="text-lg font-thin text-gray-700">Mentores</p>
                </div>
                <div class="col-span-1">
                    <p class="text-4xl">300+</p>
                    <p class="text-lg font-thin text-gray-700">Asesorias</p>
                </div>
            </div>
        </article>
    </section>
</template>
