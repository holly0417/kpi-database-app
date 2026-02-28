<template>
  <q-form>
    <div class="q-pa-md">
      <div class="q-gutter-md col">
        <q-badge color="secondary" multi-line>
          Enter new KPI: {{ thisKpi }}
        </q-badge>
        <q-input filled v-model="formData.name" label="Name" stack-label :dense="true" lazy-rules
          :rules="[ val => val && val.length > 0 || 'Please type something']"/>
        <q-input filled v-model="formData.description" label="Notes & explanations" stack-label type="textarea"/>
        <q-input filled v-model="formData.formula" label="Formula" stack-label :dense="true" />
        <q-input filled v-model="formData.unit" label="Unit" stack-label :dense="true" />
        <q-input filled v-model="formData.frequency" label="Frequency" stack-label :dense="true" />
      </div>
      <div class="q-gutter-md row justify-center">
        <q-badge color="secondary" multi-line>
          Select the usually desired direction of KPI 
          <br>(i.e., Select "Up" if a higher numerical indicator is always better than a lower one. 
          <br>Select "Target" if it's better to stay around benchmark.)
        </q-badge>
        <q-radio v-model="formData.direction" emit-value val="up" label="Up" @update:model-value="setDirection" />
        <q-radio v-model="formData.direction" emit-value val="down" label="Down" @update:model-value="setDirection" />
        <q-radio v-model="formData.direction" emit-value val="target" label="Target" @update:model-value="setDirection" />
      </div>
    </div>
  </q-form>


  <div class="q-pa-md column items-center">
    <div class="q-gutter-md row">
      <q-btn style="background: #4AA191; color: white" label="SUBMIT KPI" @click="enterNewKPI" />
      <q-btn style="background: #E89058; color: white" label="CLEAR FORM" @click="clearKPIs" />  
    </div>
  </div>

  
  <q-table
      flat bordered
      grid
      title="KPIs"
      :rows="rows"
      :columns="columns"
      row-key="name"
      :filter="filter"
      hide-header
      :rows-per-page-options="[4]"
    >
    <template v-slot:top-right>
      <q-input borderless dense debounce="300" v-model="filter" placeholder="Search">
        <template v-slot:append>
          <q-icon name="search" />
        </template>
      </q-input>
    </template>
  </q-table>
</template>
<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { QForm } from 'quasar';
import type { kpiToAdd, KpiIndustryToAdd, KpiIndustryList } from 'src/components/models';
import { Direction } from 'src/components/models';
import { getAllKPIIndustry, fetchGICSLayersBySubIndustry, addKPI, addKPIIndustry } from "src/services/exampleService";
import type { GICSResponse } from 'src/components/models';

const props = defineProps<{
  subindustryToMatch: GICSResponse;
}>();

const formData = ref<kpiToAdd>({
  name: '',
  description: '',
  formula: '',
  unit: '',
  direction: Direction.DOWN,
  frequency: ''
});

const thisKpi = ref<kpiToAdd>();
const rows = ref<KpiIndustryList[]>([]);
const filter = ref();

const columns = [
  { name: 'name', label: 'Name', field: 'name', sortable: true},
  { name: 'description', label: 'Description', field: 'description'},
  { name: 'formula', label: 'Formula', field: 'formula'},
  { name: 'unit', label: 'Unit', field: 'unit', sortable: true},
  { name: 'direction', label: 'Direction', field: 'direction', sortable: true},
  { name: 'frequency', label: 'Frequency', field: 'frequency', sortable: true},
  { name: 'sub_industry', label: 'Subindustry', field: 'sub_industry', sortable: true},
  { name: 'industry', label: 'Industry', field: 'industry', sortable: true},
  { name: 'industry_group', label: 'Industry Group', field: 'industry_group', sortable: true},
  { name: 'sector', label: 'Sector', field: 'sector', sortable: true}
]

onMounted(async () => {
  try {
    rows.value = await getAllKPIIndustry();
  } catch (err) {
    console.error(err);
  }
});

async function enterNewKPI() {
  if(props.subindustryToMatch.code == 0){
    console.log("enterNewKPI function needs selected subindustry to match to");
    return;
  }

  const allSelectedGICSLayers = await fetchGICSLayersBySubIndustry(props.subindustryToMatch.code);

  console.log('subindustry:', allSelectedGICSLayers.sub_industry.id);
  console.log('industry:', allSelectedGICSLayers.industry.id);
  console.log('industry group:', allSelectedGICSLayers.industry_group.id);
  console.log('sector:', allSelectedGICSLayers.sector.id);

  thisKpi.value = formData.value;
  const newKPIId = await addKPI(thisKpi.value);

  const kpiIndustryToAdd = ref<KpiIndustryToAdd>({
    kpi: newKPIId.id,
    sector: allSelectedGICSLayers.sector.id,
    industry_group: allSelectedGICSLayers.industry_group.id,
    industry: allSelectedGICSLayers.industry.id,
    sub_industry: allSelectedGICSLayers.sub_industry.id,
  });

  console.log('kpiIndustryToAdd:', kpiIndustryToAdd);
  const response = await addKPIIndustry(kpiIndustryToAdd.value);
  rows.value = await getAllKPIIndustry();
  clearKPIs();
  console.log('response:', response);
  // console.log("successfully called enterNewKPI function");
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

function clearKPIs() {
  formData.value = {
    name: '',
    description: '',
    formula: '',
    unit: '',
    direction: Direction.DOWN,
    frequency: ''
  };
}



</script>
