<template>
  <div class="row">
    <div class="col">
      <p>All sectors</p>
    <ul>
      <li v-for="sector in allSectors" :key="sector.code" @click="increment">
        {{ sector.code }} - {{ sector.name }}
      </li>
    </ul>
    </div>

    <div class="col">
      <p>Industry Group for sector code 25</p>
    <ul>
      <li v-for="group in someIndustryGroups" :key="group.code" @click="increment">
        {{ group.code }} - {{ group.name }}
      </li>
    </ul>
    </div>

    <div class="col">
    <p>Industries for industry group code 2510</p>
    <ul>
      <li v-for="industry in someIndustries" :key="industry.code" @click="increment">
        {{ industry.code }} - {{ industry.name }}
      </li>
    </ul>
    </div>

    <div class="col">
      <p>Subindustries for industry code 251010</p>
    <ul>
      <li v-for="subindustry in someSubIndustries" :key="subindustry.code" @click="increment">
        {{ subindustry.code }} - {{ subindustry.name }}
      </li>
    </ul>
    </div>
  
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import type { GICSResponse } from 'src/components/models';
import { fetchGICS, fetchGICSIndustryGroups, fetchGICSIndustries, fetchGICSSubIndustries } from "src/services/exampleService";

const allSectors = ref<GICSResponse[]>();
const someIndustryGroups = ref<GICSResponse[]>();
const someIndustries = ref<GICSResponse[]>();
const someSubIndustries = ref<GICSResponse[]>();

const clickCount = ref(0);
function increment() {
  clickCount.value += 1;
  return clickCount.value;
}

onMounted(async () => {
  try {
    allSectors.value = await fetchGICS();
    someIndustryGroups.value = await fetchGICSIndustryGroups(25);
    someIndustries.value = await fetchGICSIndustries(2510);
    someSubIndustries.value = await fetchGICSSubIndustries(251010);
  } catch (err) {
    console.error(err);
  }
});

</script>
