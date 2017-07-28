<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import NavPrimary from './components/_NavPrimary.vue';

export default {
  name: 'app',
  components: {
    NavPrimary,
  },
};
</script>

<style lang="scss">
@import '~normalize.css/normalize.css';
#app {}
</style>
