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
.layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;

  #header {
    flex: 0;
  }
  #breadcrumb {}
  main {
    flex: 1;
  }
  #footer {
    flex: 0;
  }
}
</style>
