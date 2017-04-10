<template>
  <header id="header" class="wrapper">
    <div id="branding">
        <span>Visualist</span>
    </div>
    <nav id="site_nav">
      <span class="header">Menu</span>
      <ul>
        <li><router-link :to="{ name: 'home'}">Home</router-link></li>
        <li><router-link :to="{ name: 'events'}">Events</router-link></li>
        <li>Search</li>
      </ul>
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
    #site_nav {}
  }
</style>
