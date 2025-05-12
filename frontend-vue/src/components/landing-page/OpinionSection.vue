<script setup>
import NeoContainer from '../NeoContainer.vue';
</script>

<template>
    <section class="mt-50">
        <NeoContainer bg="bg-[#96FEAD]" class="grid grid-cols-2 gap-4 p-6 h-[540px]">
            <header class="flex flex-col p-6">
                <h3 class="font-ppgosha font-bold text-2xl 2xl:text-4xl mb-4">
                    Opiniones de nuestra comunidad
                </h3>
                <p class="lg:text-base 2xl:text-lg">
                    Cada historia cuenta. Estas son algunas experiencias reales de personas que, como tú, decidieron
                    crecer aprendiendo junto a otros. Descubre lo que nuestra comunidad tiene para decir sobre
                    Mentor-U.
                </p>
                <div class="flex items-center justify-center mt-18 -rotate-15">
                    <img src="../../assets/images/comments.png" class="lg:w-86 2xl:w-[400px]" alt="Developer Image" />
                </div>
            </header>

            <div class="relative">
                <div class="grid grid-cols-1 gap-4 absolute -top-25">
                    <NeoContainer bg="bg-white" class="flex flex-col gap-2 p-4">
                        <article>
                            <p class="lg:text-base 2xl:text-lg">
                                He usado Mentor-U durante seis meses para aprender Python y quedé impresionado con lo
                                fácil
                                que es contactar con las personas expertas. Lo recomiendo 100%.
                            </p>
                            <div class="flex my-2 text-yellow-500">
                                <span class="material-symbols-rounded" style="font-size: 1.2rem;">star</span>
                                <span class="material-symbols-rounded" style="font-size: 1.2rem;">star</span>
                                <span class="material-symbols-rounded" style="font-size: 1.2rem;">star</span>
                                <span class="material-symbols-rounded" style="font-size: 1.2rem;">star</span>
                                <span class="material-symbols-rounded" style="font-size: 1.2rem;">star</span>
                            </div>
                            <footer>
                                <p class="font-bold lg:text-lg 2xl:text-xl">Pedro N.</p>
                            </footer>
                        </article>
                    </NeoContainer>

                    <NeoContainer bg="bg-white" class="flex flex-col gap-2 p-4">
                        <article>
                            <p class="lg:text-base 2xl:text-lg">
                                Gracias a Mentor-U encontré una mentora que me ayudó a preparar entrevistas técnicas.
                                Hoy
                                trabajo como desarrolladora frontend y no estaría aquí sin esa guía.
                            </p>
                            <div class="flex my-2 text-yellow-500">
                                <span class="material-symbols-rounded" style="font-size: 1.2rem;">star</span>
                                <span class="material-symbols-rounded" style="font-size: 1.2rem;">star</span>
                                <span class="material-symbols-rounded" style="font-size: 1.2rem;">star</span>
                                <span class="material-symbols-rounded" style="font-size: 1.2rem;">star</span>
                                <span class="material-symbols-rounded" style="font-size: 1.2rem;">star</span>
                            </div>
                            <footer>
                                <p class="font-bold lg:text-lg 2xl:text-xl">Lucía M.</p>
                            </footer>
                        </article>
                    </NeoContainer>

                    <NeoContainer bg="bg-white" class="flex flex-col gap-2 p-4">
                        <article>
                            <p class="lg:text-base 2xl:text-lg">
                                Como mentor, me encanta poder compartir lo que sé con estudiantes motivados. La
                                plataforma
                                facilita todo y hace que el proceso sea muy satisfactorio.
                            </p>
                            <div class="flex my-2 text-yellow-500">
                                <span class="material-symbols-rounded" style="font-size: 1.2rem;">star</span>
                                <span class="material-symbols-rounded" style="font-size: 1.2rem;">star</span>
                                <span class="material-symbols-rounded" style="font-size: 1.2rem;">star</span>
                                <span class="material-symbols-rounded" style="font-size: 1.2rem;">star</span>
                                <span class="material-symbols-rounded" style="font-size: 1.2rem;">star</span>
                            </div>
                            <footer>
                                <p class="font-bold lg:text-lg 2xl:text-xl">Carlos G.</p>
                            </footer>
                        </article>
                    </NeoContainer>
                </div>
            </div>
        </NeoContainer>
    </section>
</template>