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
</style>
