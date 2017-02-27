<template>
  <div id="home" class="container">
    <h1>{{ pageTitle }}</h1>
    <p>{{ pageSubtitle }}</p>
  </div>
</template>

<script>
export default {
  name: 'home',
  data() {
    return {
      pageTitle: 'Home',
      pageSubtitle: 'This is the home page.',
    };
  },
};
</script>

<style lang="scss" scoped>
</style>
