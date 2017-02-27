<template>
  <div id="nodes">
    <node-cards></node-cards>
  </div>
</template>

<script>
import NodeCards from './NodeCards';

export default {
  name: 'node-list',
  data() {
    return {
      pageTitle: 'Nodes',
      pageSubtitle: 'Here are some nodes.',
    };
  },
  components: {
    NodeCards,
  },
};
</script>

<style lang="scss" scoped>
</style>
