<template>
  <div class="vis-header">
      <nav-primary></nav-primary>
      <nav-secondary></nav-secondary>
  </div>
</template>

<script>
import NavPrimary from './_NavPrimary.vue';
import NavSecondary from './_NavSecondary.vue';

export default {
  name: 'vis-header',
  components: {
    NavPrimary,
    NavSecondary,
  },
};
</script>

<style scoped>

</style>
