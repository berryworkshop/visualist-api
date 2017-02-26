<template>
  <div id="nodes" class="container">
    <h1>{{ title }}</h1>
    <p>{{ subtitle }}</p>
    <node-cards></node-cards>
  </div>
</template>

<script>
import NodeCards from '../NodeCards';

export default {
  name: 'node-list',
  data() {
    return {
      title: 'Nodes',
      subtitle: 'Here are some nodes.',
    };
  },
  components: {
    NodeCards,
  },
};
</script>

<style lang="scss" scoped>
</style>
