<template>
  <div class="panel" id="home">
    <p>Here's home page stuff.</p>
  </div>
</template>

<script>
export default {
  name: 'home',
  data() {
    return {};
  },
  mounted() {
    this.$store.commit('resetPageData');
  },
};
</script>

<style lang="scss" scoped>
</style>
