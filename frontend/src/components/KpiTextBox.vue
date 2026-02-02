<template>
  <q-form>
      <div class="q-pa-md">
        <div class="q-gutter-md row items-start">
          <q-badge color="secondary" multi-line>
            KPI: {{ thisKpi }}
          </q-badge>
        </div>
        <div class="q-gutter-md row items-start">
          <q-input filled v-model="formData.name" label="Name" stack-label :dense="true" />
          <q-input filled v-model="formData.description" label="Description" stack-label :dense="true" />
          <q-input filled v-model="formData.formula" label="Formula" stack-label :dense="true" />
          <q-input filled v-model="formData.unit" label="Unit" stack-label :dense="true" />
          <q-input filled v-model="formData.direction" label="Direction" stack-label :dense="true" />
          <q-input filled v-model="formData.frequency" label="Frequency" stack-label :dense="true" />
        </div>
    </div>
  </q-form>
</template>
<script setup lang="ts">
import { ref, watch, computed } from 'vue';
import { QForm } from 'quasar';
import type { Kpi } from 'src/components/models';

const props = defineProps({
  enterKPI: {
    type: Boolean,
    default: false,
  },
  clearKPI: {
    type: Boolean,
    default: false,
  },
})

const thisKpi = ref<Kpi>();

const formData = ref<Kpi>({
  name: '',
  description: '',
  formula: '',
  unit: '',
  direction: '',
  frequency: ''
});

watch(
  () => props.enterKPI,
  (newVal) => {
    if (newVal === true) {
      enterNewKPI()
    }
  },
  { immediate: true }
)

function enterNewKPI() {
  if (props.enterKPI == true) {
    console.log("successfully called enterNewKPI function");
    thisKpi.value = formData.value;
  }
};

const resetForm = () => {
  formData.value.name = '';
  formData.value.description = '';
  formData.value.formula = '';
  formData.value.unit = '';
  formData.value.direction = '';
  formData.value.frequency = ''
}

</script>
