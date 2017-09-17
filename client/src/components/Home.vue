<template>
  <div class="hello">
    <h2>Home</h2>
    <ul>
      <li><router-link :to="{name: 'directory'}">Directory</router-link></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'home',
};
</script>

<style lang="scss" scoped>
</style>

