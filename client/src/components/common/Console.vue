<template>
  <div class="console">
    <h1 id="brand"><router-link :to="{name: 'home'}">The Visualist</router-link></h1>
    <p>Chicago's Visual Arts Calendar</p>

    <nav id="primary-nav">
      <ul>
        <li><router-link :to="{name: 'calendar'}">Calendar</router-link></li>
        <li><router-link :to="{name: 'directory'}">Directory</router-link></li>
        <li><router-link :to="{name: 'map'}">Map</router-link></li>
      </ul>
    </nav>
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

  a {
    color: orange;
    &:hover, &:active, &:visited {
      color: coral;
    }
    text-decoration: none;
  }

  padding: 1rem;
  #brand {
    a {
      color: white;
      text-decoration: none;
    }
  }
  #primary-nav {
    ul {
      list-style-type: none;
      padding-left: 0;
    }
  }
}
</style>
