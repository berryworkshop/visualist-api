<template>
  <header id="header" class="wrapper">
    <div id="branding">
        <span>Visualist</span>
    </div>
    <nav id="primary_nav">
        <span>
            Browse
        </span>
        <span>
            Search
        </span>
    </nav>
  </header>
</template>


<script>
export default {
  name: 'site-header',
  data() {
    return {};
  },
};
</script>

<style lang="scss" scoped>
  header {
    display: flex;

    #branding {}
    #primary_nav {
      text-align: right;
    }
  }
</style>
