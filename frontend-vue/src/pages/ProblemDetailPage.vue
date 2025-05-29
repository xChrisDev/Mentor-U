<template>
  <div v-if="problem" class="mx-auto flex justify-center py-10" data-aos="zoom-in" data-aos-delay="100">
    <div class="w-[90%] lg:w-[85%] grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="lg:col-span-1 space-y-4">
        <NeoContainer bg="bg-white" class="flex flex-col p-6 space-y-4">
          <div>
            <div class="flex flex-col gap-2 pb-2">
              <h1 class="text-2xl font-bold">{{ problem.title }}</h1>
              <div class="flex gap-2">
                <NeoTab :text="getDifficultyText(problem.difficulty)" :bg="getDifficultyColor(problem.difficulty)"
                  icon="trending_up" />
                <NeoTab :text="problem.topic" bg="bg-[#E6E6FA]" icon="category" />
                <NeoTab :text="problem.lang" bg="bg-[#FFD6A5]" icon="code" />
              </div>
            </div>
            <p class="font-medium text-gray-700 mt-1">{{ problem.description }}</p>
          </div>

          <div>
            <h3 class="font-bold mb-2">Restricciones</h3>
            <NeoContainer bg="bg-[#EBDFFF]" class="p-4 border border-black shadow-none">
              <p class="text-md text-gray-600">{{ problem.constraints }}</p>
            </NeoContainer>
          </div>

          <div v-if="problem.examples.length">
            <h3 class="font-bold mb-2">Ejemplos</h3>
            <div v-for="(ex, i) in problem.examples" :key="i"
              class="bg-[#FFEECE] border-2 border-black rounded-lg p-4 mb-2">
              <p class="text-md text-gray-600 font-medium"><span class="font-bold text-black">Entrada:</span> {{
                ex.input }}</p>
              <p class="text-md text-gray-600 font-medium"><span class="font-bold text-black">Salida esperada:</span> {{
                ex.output }}</p>
            </div>
          </div>
        </NeoContainer>
      </div>

      <div class="lg:col-span-2 space-y-4">
        <NeoContainer bg="bg-white" class="p-6 space-y-4 flex flex-col">
          <h3 class="font-bold text-xl">Escribe tu solución</h3>
          <MonacoEditor v-model="userCode" :language="problem.lang.toLowerCase() || 'javascript'" />

          <div class="flex justify-end gap-4">
            <div class="flex justify-end gap-4">
              <NeoButton :disabled="isEval || problem.status === 'in_revision' || problem.status === 'completed'"
                text="Probar Código" bg="#D0F4FF" icon="play_arrow" @click="testingCode" />
              <NeoButton :disabled="!isTested || problem.status === 'in_revision' || problem.status === 'completed'"
                text="Enviar Solución" bg="#96FEAD" icon="send" @click="submitSolution" />
            </div>

          </div>
        </NeoContainer>

        <div v-if="isEval" class="border-2 border-black p-6 bg-white rounded-lg flex justify-center items-center">
          <div class="loader"></div>
        </div>

        <NeoContainer v-if="result" bg="bg-white" class="p-4 flex flex-col" data-aos="fade-up" data-aos-delay="100">
          <h3 class="font-bold">Resultado</h3>

          <div v-if="Array.isArray(result.message.results)">
            <div v-for="(test, i) in result.message.results" :key="i" class="border border-black rounded-lg p-4 my-2"
              :class="test.passed ? 'bg-[#96FEAD]' : 'bg-[#FFADAD]'">
              <p><strong>#{{ i + 1 }}</strong></p>
              <p class="font-medium text-gray-700"><strong class="text-black">Entrada:</strong> {{ test.input }}</p>
              <p class="font-medium text-gray-700"><strong class="text-black">Salida esperada:</strong> {{
                test.expected_output }}</p>
              <p class="font-medium text-gray-700"><strong class="text-black">Salida obtenida:</strong> {{
                test.actual_output }}</p>
              <p>
                <strong>Resultado: </strong>
                <span :class="test.passed ? 'text-green-700' : 'text-red-700'">
                  {{ test.passed ? 'Correcto' : 'Incorrecto' }}
                </span>
              </p>
            </div>
          </div>
        </NeoContainer>

        <NeoContainer bg="bg-gray-400" v-if="problem.status === 'in_revision'"
          class="p-4 flex justify-center items-center">
          <span class="material-symbols-rounded me-2" style="font-size: 2rem;">
            schedule
          </span>
          <h3 class="font-bold text-2xl">Actualmente tu problema está en revisión por el mentor.</h3>
        </NeoContainer>

        <NeoContainer bg="bg-green-300" v-if="problem.status === 'completed'"
          class="p-4 flex justify-center items-center">
          <span class="material-symbols-rounded me-2" style="font-size: 2rem;">
            check_circle
          </span>
          <h3 class="font-bold text-2xl">Ya has completado esté problema correctamente.</h3>
        </NeoContainer>
      </div>
    </div>
  </div>
</template>


<script setup>
import { onMounted, ref } from 'vue';
import NeoContainer from '../components/NeoContainer.vue';
import NeoButton from '../components/NeoButton.vue';
import NeoTab from '../components/NeoTab.vue';
import MonacoEditor from '../components/MonacoEditor.vue';
import { getProblemByID, postStudentSolution, updateProblemStatus } from '../services/problemService';
import { useAuth } from '../composables/useAuth';
import { testCode } from '../services/problemService';
import { useToast } from 'vue-toastification';

const props = defineProps({
  id: String,
  id_mentorie: String,
  id_problem: String
});

const { fetchUser } = useAuth()
const problem = ref(null)
const userCode = ref('');
const result = ref(null);
const isTested = ref(false);
const isEval = ref(false);
const toast = useToast()

const getDifficultyColor = (difficulty) => {
  switch (difficulty) {
    case 'facil': return 'bg-[#96FEAD]';
    case 'medio': return 'bg-[#FFD6A5]';
    case 'dificil': return 'bg-[#FFADAD]';
    default: return 'bg-gray-300';
  }
};

const getDifficultyText = (difficulty) => {
  switch (difficulty) {
    case 'facil': return 'Fácil';
    case 'medio': return 'Medio';
    case 'dificil': return 'Difícil';
    default: return 'Desconocido';
  }
};

const testingCode = async () => {
  isEval.value = true;
  const res = await testCode({
    lang: problem.value.lang,
    code: userCode.value,
    examples: problem.value.examples
  });
  console.log(res);
  result.value = res;

  const passedAll = Array.isArray(res.message.results)
    ? res.message.results.every(test => test.passed)
    : false

  isTested.value = passedAll
  isEval.value = false
};


const submitSolution = async () => {
  try {
    const user = await fetchUser();
    await updateProblemStatus(props.id_problem, { problem_id: props.id_problem, student_id: user.data.id, status: 'in_revision' })
    await postStudentSolution({ problem_id: props.id_problem, student_id: user.data.id, code: userCode.value, mentorie_id: props.id_mentorie, comments: '', result: 'pending' })
    toast.success("Solución enviada correctamente al mentor", {
      toastClassName: "my-custom-toast-class",
    });
    isTested.value = false
  } catch (error) {
    console.log(error)
    toast.error("Error al enviar", {
      toastClassName: "my-custom-toast-class",
    });
  }
};

onMounted(async () => {
  const res = await fetchUser();
  problem.value = await getProblemByID(props.id_problem, res.data.id)
  // console.log(problem.value)
})
</script>
