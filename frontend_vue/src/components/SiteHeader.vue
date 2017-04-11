<template>
  <header class="site-header container">
    <div class="row">
      <div id="branding" class="column">
          <span>Visualist</span>
      </div>
      <nav id="site_nav" class="column">
        <span class="header">Menu</span>
        <ul>
          <li><router-link :to="{ name: 'home'}">Home</router-link></li>
          <li><router-link :to="{ name: 'events'}">Events</router-link></li>
          <li>Search</li>
        </ul>
      </nav>
    </div>
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
