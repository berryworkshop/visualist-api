<template>
  <div id="app">
    <site-header></site-header>
    <site-main></site-main>
    <site-footer></site-footer>
  </div>
</template>

<script>
import SiteHeader from './components/SiteHeader';
import SiteMain from './components/SiteMain';
import SiteFooter from './components/SiteFooter';

export default {
  name: 'app',
  data() {
    return {};
  },
  components: {
    SiteHeader,
    SiteMain,
    SiteFooter,
  },
};
</script>


<style lang="scss">
  @import "~normalize.css";

  // box-sizing: https://css-tricks.com/box-sizing/
  html {
    box-sizing: border-box;
  }
  *, *:before, *:after {
    box-sizing: inherit;
  }

  body {
    margin: 0;
  }

  .wrapper {
    max-width: 1000px;
    background-color: silver;
    margin-left: auto;
    margin-right: auto;
    display: flex;
  }

  .content {
    /* mobile */

    /* desktop */
    @media (min-width: 500px) {
    }
  }

  .controls {
    /* mobile */

    /* desktop */
    @media (min-width: 500px) {
    }
  }

</style>
