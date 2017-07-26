<template>
  <div id="app">
    <nav-primary></nav-primary>
    <router-view></router-view>
  </div>
</template>

<script>
import NavPrimary from './components/_NavPrimary';

export default {
  name: 'app',
  components: {
    NavPrimary,
  },
};
</script>

<style>
#app {}
</style>
