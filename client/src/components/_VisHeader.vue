<template>
  <div class="vis-header">
    <ul>
        <nav-primary></nav-primary>
        <nav-secondary></nav-secondary>
    </ul>
  </div>
</template>

<script>
import NavPrimary from './_NavPrimary';
import NavSecondary from './_NavSecondary';

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
