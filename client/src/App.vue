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
@import './assets/global.scss';


#app {
  background-color: hsl(0, 0, 95%);

  min-height: 100vh;
  display: flex;
  flex-direction: column;
  #console {
    flex: 0;
  }
  #layout {
    flex: 1;
  }
  @include screen_tablet_landscape_up {
    flex-direction: row;
    #console {
      flex-basis: 16rem;
      min-height: 100vh;
      height: inherit;
    }
    #layout {
      min-height: 100vh;
    }
  }
}
</style>
