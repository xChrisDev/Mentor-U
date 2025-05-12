<script setup>
import NeoContainer from '../NeoContainer.vue';
</script>

<template>
    <footer class="mt-20">
        <NeoContainer bg="bg-[#EBDFFF]" class="flex flex-col gap-8 p-8 rounded-2xl">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div>
                    <div class="flex items-center mb-3">
                        <span class="material-symbols-rounded text-4xl me-2">school</span>
                        <h1 class="font-ppgosha text-2xl">Mentor-U</h1>
                    </div>
                    <p class="text-base font-normal max-w-xs lg:text-sm 2xl:text-base">
                        Aprende con mentoría personalizada en tu lenguaje de programación favorito. Comunidad,
                        tecnología y crecimiento, todo en un solo lugar.
                    </p>
                </div>

                <div class="flex flex-col gap-2">
                    <h3 class="font-semibold mb-1 text-2xl font-ppgosha">Enlaces rápidos</h3>
                    <a href="#" class="hover:underline font-normal">Inicio</a>
                    <a href="#" class="hover:underline font-normal">Explorar tecnologías</a>
                    <a href="#" class="hover:underline font-normal">Beneficios</a>
                    <a href="#" class="hover:underline font-normal">Testimonios</a>
                </div>

                <div class="flex flex-col gap-2">
                    <h3 class="font-semibold mb-1 text-2xl font-ppgosha">Contacto</h3>
                    <p class="text-base">Email: <a href="mailto:contacto@mentor-u.com"
                            class="hover:underline font-normal">contacto@mentor-u.com</a></p>
                    <p class="text-base">Soporte: <a href="#" class="hover:underline font-normal">Centro de ayuda</a>
                    </p>
                    <p class="text-base">Privacidad: <a href="#" class="hover:underline font-normal">Política y
                            términos</a></p>
                </div>
            </div>

            <div class="flex justify-between items-center border-t pt-4 flex-wrap gap-4">
                <p class="text-sm text-gray-600">&copy; 2025 Mentor-U. Todos los derechos reservados.</p>
                <div class="flex gap-4">
                    <a href="#" aria-label="Facebook" class="hover:opacity-80">
                        <img src="../../assets/icons/facebook.svg" alt="Facebook" class="w-6 h-6" />
                    </a>
                    <a href="#" aria-label="Instagram" class="hover:opacity-80">
                        <img src="../../assets/icons/instagram.svg" alt="Instagram" class="w-6 h-6" />
                    </a>
                    <a href="#" aria-label="Twitter" class="hover:opacity-80">
                        <img src="../../assets/icons/twitter.svg" alt="Twitter" class="w-6 h-6" />
                    </a>
                </div>
            </div>
        </NeoContainer>
    </footer>
</template>
