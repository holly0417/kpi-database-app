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
          <q-radio v-model="formData.direction" emit-value val="up" label="Up" @update:model-value="setDirection" />
          <q-radio v-model="formData.direction" emit-value val="down" label="Down" @update:model-value="setDirection" />
          <q-radio v-model="formData.direction" emit-value val="target" label="Target" @update:model-value="setDirection" />
          <q-input filled v-model="formData.frequency" label="Frequency" stack-label :dense="true" />
        </div>
    </div>
  </q-form>
  
  <q-markup-table title="KPIs">
    <thead>
      <tr>
        <th>KPI description</th>
        <th>formula</th>
        <th>unit</th>
        <th>direction</th>
        <th>frequency</th>
      </tr>
    </thead>

    <tbody>
      <tr v-for="kpi in thisRows"
          :key="kpi.name" class="text-center">
          <td v-text="kpi.description"></td>
          <td v-text="kpi.formula"></td>
          <td v-text="kpi.unit"></td>
          <td v-text="kpi.direction"></td>
          <td v-text="kpi.frequency"></td>
      </tr>
    </tbody>

  </q-markup-table>

</template>
<script setup lang="ts">
import { ref, watch, onMounted } from 'vue';
import { QForm } from 'quasar';
import type { Kpi } from 'src/components/models';
import { Direction } from 'src/components/models';
import { addKPI, getKPI } from "src/services/exampleService";

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

const formData = ref<Kpi>({
  name: '',
  description: '',
  formula: '',
  unit: '',
  direction: Direction.DOWN,
  frequency: ''
});


const thisKpi = ref<Kpi>();
const thisRows  = ref<Kpi[]>([]);

onMounted(async () => {
  try {
    thisRows.value = await getKPI();
  } catch (err) {
    console.error(err);
  }
});


watch(
  () => props.enterKPI,
  async (newVal) => {
    if (newVal === true) {
        await enterNewKPI();
    }
  },
  { immediate: true }
)


const enterNewKPI = async () => {
  if (props.enterKPI == true) {
    console.log("successfully called enterNewKPI function");
    thisKpi.value = formData.value;
    await addKPI(thisKpi.value);
  }
};
      
function setDirection(direction: string) {
  if(direction == "up") {
    formData.value.direction = Direction.UP;
  } 
  
  if(direction == "down") {
    formData.value.direction = Direction.DOWN;
  }

  if(direction == "target") {
    formData.value.direction = Direction.TARGET;
  }
}

</script>
