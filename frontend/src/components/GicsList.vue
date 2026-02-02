<template>
      <div class="q-pa-md">
        <div class="q-gutter-md row items-start">
          <div class="col">
            <q-badge color="secondary" multi-line>
              Sector: {{ thisSector }}
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
              Industry Group: {{ thisIndustryGroup }}
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
              Industry: {{ thisIndustry }}
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
              Subindustry: {{ thisSubIndustry?.code }}
            </q-badge>

            <q-select filled 
            v-model="thisSubIndustry" 
            :options="someSubIndustries"
            option-value="code"
            option-label="name" 
            style="min-width: 250px; max-width: 300px"
            />
          </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { watch, ref, onMounted } from 'vue';
import type { GICSResponse } from 'src/components/models';
import { fetchGICS, fetchGICSIndustryGroups, fetchGICSIndustries, fetchGICSSubIndustries } from "src/services/exampleService";

const props = defineProps({
  clearClassifiers: {
    type: Boolean,
    default: false,
  },
})

const allSectors = ref<GICSResponse[]>();
const someIndustryGroups = ref<GICSResponse[]>();
const someIndustries = ref<GICSResponse[]>();
const someSubIndustries = ref<GICSResponse[]>();

const thisSector = ref<GICSResponse>();
const thisIndustryGroup = ref<GICSResponse>();
const thisIndustry = ref<GICSResponse>();
const thisSubIndustry = ref<GICSResponse>();

onMounted(async () => {
  try {
    allSectors.value = await fetchGICS();
  } catch (err) {
    console.error(err);
  }
});

watch(
  () => props.clearClassifiers,
  (newVal) => {
    if (newVal === true) {
      resetClassifiers()
    }
  },
  { immediate: true }
)

function resetClassifiers(){
  someIndustryGroups.value = [];
  someIndustries.value = [];
  someSubIndustries.value = [];

  thisSector.value = {
    code: "",
    name: ""
  };

  thisIndustryGroup.value = {
    code: "",
    name: ""
  };

  thisIndustry.value = {
    code: "",
    name: ""
  };

  thisSubIndustry.value = {
    code: "",
    name: ""
  };
}

async function getIndustryGroupList(sectorCode: string) {
  const codeToNumber = Number(sectorCode)
  someIndustryGroups.value = await fetchGICSIndustryGroups(codeToNumber);

  thisIndustryGroup.value = {
    code: sectorCode,
    name: ""
  };

  thisIndustry.value = {
    code: "",
    name: ""
  };

  thisSubIndustry.value = {
    code: "",
    name: ""
  };

  someIndustries.value = [];
  someSubIndustries.value = [];
}

async function getIndustryList(industryGroupCode: string) {
  const codeToNumber = Number(industryGroupCode)
  someIndustries.value = await fetchGICSIndustries(codeToNumber);

  thisIndustry.value = {
    code: industryGroupCode,
    name: ""
  };

  thisSubIndustry.value = {
    code: "",
    name: ""
  };

  someSubIndustries.value = [];
}

async function getSubIndustryList(industryCode: string) {
  const codeToNumber = Number(industryCode)
  someSubIndustries.value = await fetchGICSSubIndustries(codeToNumber);

  thisSubIndustry.value = {
    code: industryCode,
    name: ""
  };
}


</script>
