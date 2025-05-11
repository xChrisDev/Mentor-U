<script setup>
</script>

<template>
  <div class="relative min-h-screen w-full mb-4">
    <div class="absolute inset-0 -z-10 h-full w-full
             bg-white
             bg-[radial-gradient(#edd_2px,transparent_1px)]
             [background-size:24px_24px]">
    </div>

    <main class="container mx-auto w-[75%] pt-8">
      <RouterView />
    </main>
  </div>
</template>
