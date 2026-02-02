<template>
  <q-page class="row items-center justify-evenly">
    <gics-list
    :clearClassifiers="flag"
    ></gics-list>
    <kpi-text-box
    :enterKPI="enterKPI"
    :clearKPI="clearKPI"
    >
    </kpi-text-box>
    <q-btn style="background: #FF0080; color: white" label="SUBMIT" @click="toggleButtonValue" />
    <q-btn style="background: #FF0080; color: white" label="CLEAR" @click="clearKPIs" />
  </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import GicsList from 'src/components/GicsList.vue';
import KpiTextBox from 'src/components/KpiTextBox.vue';

const flag = ref(false)
const enterKPI = ref(false)
const clearKPI = ref(false)

function toggleButtonValue() {
  if (enterKPI.value == false) {
    enterKPI.value = true;
  } else {
    enterKPI.value = false;
  }
}

function clearKPIs() {
  if (clearKPI.value == false) {
    clearKPI.value = true;
  } else {
    clearKPI.value = false;
  }
}

</script>
