<template>
  <div id="app">
    <p><router-link :to="{name: 'home'}">The Visualist</router-link></p>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
};
</script>

<style>
body{
  font-size: 18px;
}

#app {
  font-family: 'Work Sans', sans-serif;
}
</style>
