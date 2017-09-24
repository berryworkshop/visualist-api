<template>
  <div id="app">
    <console id="console"></console>
    <router-view id="layout"></router-view>
  </div>
</template>

<script>
import Console from './components/common/Console';

export default {
  name: 'app',
  components: {
    Console,
  },
};
</script>

<style lang="scss">
@import '~normalize.css/normalize.css';

body * {
  box-sizing: border-box;
}

body {
  font-family: 'Roboto Mono', monospace;
  background-color: hsl(0, 0, 95%);
  color: hsl(0, 0, 20%);
  font-size: 14px;

  .container {
    padding: 1rem;
  }
}



#app {
  display: flex;
  flex-direction: row;
  min-height: 100vh;

  #console {
    flex-basis: 16rem;
    min-height: 100vh;
    height: 100%;
  }
  #layout {
    flex: 1;
    min-height: 100vh;
  }
}

</style>
