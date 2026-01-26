<template>
  <q-page class="row items-center justify-evenly">
    <example-component
      title="Example component"
      active
      :todos="todos"
      :meta="meta"
    ></example-component>
    <gics-list
      :allSectors="allSectors"
    ></gics-list>
  </q-page>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import type { Todo, Meta } from 'components/models';
import ExampleComponent from 'components/ExampleComponent.vue';
import GicsList from 'src/components/GicsList.vue';
import { fetchGICS } from "src/services/exampleService";
import type { GICSResponse } from 'src/components/models';

const allSectors = ref<GICSResponse[]>();

const todos = ref<Todo[]>([
  {
    id: 1,
    content: 'test again?',
  },
  {
    id: 2,
    content: 'check check 2',
  },
  {
    id: 3,
    content: 'ct3',
  },
  {
    id: 4,
    content: 'ct4',
  },
  {
    id: 5,
    content: 'ct5',
  },
]);

const meta = ref<Meta>({
  totalCount: 1200,
});

onMounted(async () => {
  try {
    allSectors.value = await fetchGICS();
  } catch (err) {
    console.error(err);
  }
});

</script>
