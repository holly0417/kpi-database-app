<template>
    <div class="row">
      <div class="col"></div>
      <div class="q-pa-md col-8">
        <div class="q-gutter-md row items-start">
          <div class="col">
            <q-badge color="secondary" multi-line>
              Sector
            </q-badge>

            <q-select filled 
            v-model="thisSector" 
            :options="allSectors"
            option-value="code"
            option-label="name" 
            emit-value
            map-options
            style="min-width: 250px; max-width: 300px"
            @update:model-value="getIndustryGroupList"
            />
          </div>

          <div class="col">
            <q-badge color="secondary" multi-line>
              Industry Group
            </q-badge>

            <q-select filled 
            v-model="thisIndustryGroup" 
            :options="someIndustryGroups"
            option-value="code"
            option-label="name" 
            emit-value
            map-options
            style="min-width: 250px; max-width: 300px"
            @update:model-value="getIndustryList"
            />
          </div>

          <div class="col">
            <q-badge color="secondary" multi-line>
              Industry
            </q-badge>

            <q-select filled 
            v-model="thisIndustry" 
            :options="someIndustries"
            option-value="code"
            option-label="name" 
            emit-value
            map-options
            style="min-width: 250px; max-width: 300px"
            @update:model-value="getSubIndustryList"
            />
          </div>

          <div class="col">
            <q-badge color="secondary" multi-line>
              Subindustry
            </q-badge>

            <q-select filled 
            v-model="thisSubIndustry" 
            :options="someSubIndustries"
            option-label="name" 
            style="min-width: 250px; max-width: 300px"
            />
          </div>
        </div>
          <kpi-text-box 
          :subindustryToMatch = thisSubIndustry
          />  
      </div>
      <div class="col"></div>
    </div>
    
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import type { GICSResponse } from 'src/components/models';
import { fetchGICS, fetchGICSIndustryGroups, fetchGICSIndustries, fetchGICSSubIndustries } from "src/services/exampleService";
import KpiTextBox from 'src/components/KpiTextBox.vue';

const allSectors = ref<GICSResponse[]>([]);
const someIndustryGroups = ref<GICSResponse[]>([]);
const someIndustries = ref<GICSResponse[]>([]);
const someSubIndustries = ref<GICSResponse[]>([]);

const thisSector = ref<number | null>(null);
const thisIndustryGroup = ref<number | null>(null);
const thisIndustry = ref<number | null>(null);
const thisSubIndustry = ref<GICSResponse>({id: 0, code: 0, name: ""});

onMounted(async () => {
  try {
    allSectors.value = await fetchGICS();
  } catch (err) {
    console.error(err);
  }
});

async function getIndustryGroupList(sectorCode: number | null) {
  if (sectorCode == null) return
  thisIndustryGroup.value = null;
  thisIndustry.value = null;
  thisSubIndustry.value = {id: 0, code: 0, name: ""};
  someIndustryGroups.value = [];
  someIndustries.value = [];
  someSubIndustries.value = [];
  someIndustryGroups.value = await fetchGICSIndustryGroups(sectorCode);
}

async function getIndustryList(industryGroupCode: number | null) {
  if (industryGroupCode == null) return
  thisIndustry.value = null;
  thisSubIndustry.value = {id: 0, code: 0, name: ""};
  someIndustries.value = [];
  someSubIndustries.value = [];
  someIndustries.value = await fetchGICSIndustries(industryGroupCode);
}

async function getSubIndustryList(industryCode: number | null) {
  if (industryCode == null) return
  thisSubIndustry.value = {id: 0, code: 0, name: ""};
  someSubIndustries.value = [];
  someSubIndustries.value = await fetchGICSSubIndustries(industryCode);
}


</script>
