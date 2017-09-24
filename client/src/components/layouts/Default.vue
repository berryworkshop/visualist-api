<template>
  <div class="layout">
    <vis-header id="header"></vis-header>
    <nav-breadcrumb id="breadcrumb"></nav-breadcrumb>
    <main id="main" class="container">
      <slot></slot>
    </main>
    <vis-footer id="footer"></vis-footer>
  </div>
</template>


<script>
import VisHeader from '../common/VisHeader';
import VisFooter from '../common/VisFooter';
import NavBreadcrumb from '../common/NavBreadcrumb';

export default {
  name: 'layout-default',
  components: {
    VisHeader,
    NavBreadcrumb,
    VisFooter,
  },
};
</script>


<style lang='scss'>
@import '../../assets/global.scss';

.layout {
  display: flex;
  flex-direction: column;
  // #header {}
  // #breadcrumb {}
  main {
    flex: 1;
  }
  // #footer {}
  @include screen_tablet_landscape_up {
    min-height: 100vh;
  }
}
</style>
