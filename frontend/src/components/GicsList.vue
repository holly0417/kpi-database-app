<template>
  <div>
    <ul>
      <li v-for="sector in props.allSectors" :key="sector.code" @click="increment">
        {{ sector.code }} - {{ sector.name }}
      </li>
    </ul>
    <p>Active: {{ allSectors ? 'yes' : 'no' }}</p>
    <p>Clicks on todos: {{ clickCount }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import type { GICSResponse } from 'src/components/models';

const props = defineProps<{
  allSectors: GICSResponse[] | undefined
}>();

const clickCount = ref(0);
function increment() {
  clickCount.value += 1;
  return clickCount.value;
}

</script>
