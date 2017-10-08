<template>
  <header class="container">
    <nav id="secondary-nav">
      <ul>
        <router-link :to="{name: 'user'}">User</router-link>
        <router-link :to="{name: 'search'}">Search</router-link>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'vis-header',
};
</script>

<style lang='scss' scoped>
header {
  background-color: hsl(0, 0%, 85%);
  display: flex;
  flex-direction: row;
  align-items: baseline;

  ul {
    margin: 0;
    padding: 0;
    li {
      display: inline;
    }
  }

  #secondary-nav {
    flex: 1;
    text-align: right;
  }
}
</style>
