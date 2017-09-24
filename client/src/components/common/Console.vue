<template>
  <div class="console">
    <h1 id="brand"><router-link :to="{name: 'home'}">The Visualist</router-link></h1>
    <p>Chicago's Visual Arts Calendar</p>
  </div>
</template>


<script>
export default {
  name: 'console',
};
</script>


<style lang='scss' scoped>
.console {
  background-color: hsl(0, 0%, 5%);
  color: white;
  padding: 1rem;
  #brand {
    a {
      color: white;
      text-decoration: none;
    }
  }
}
</style>
