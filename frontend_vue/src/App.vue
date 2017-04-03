<template>
  <div id="app">

    <site-header></site-header>

    <div class="uk-section uk-section-default">
      <main class="uk-container uk-container-small">

        <ul class="uk-breadcrumb">
            <li><router-link :to="{ name: 'home'}">Home</router-link></li>
            <li class="uk-disabled"><a href="#">Disabled</a></li>
            <li><span href="#">Active</span></li>
        </ul>

        <div id="content">
          <router-view></router-view>
        </div>
      </main>
    </div>

    <site-footer></site-footer>

  </div>
</template>


<script>
import SiteHeader from './components/SiteHeader';
import SiteFooter from './components/SiteFooter';

export default {
  name: 'app',
  data() {
    return {};
  },
  components: {
    SiteHeader,
    SiteFooter,
  },
};
</script>


<style lang="scss">
// 1. Your custom variables and variable overwrites.
// $global-link-color: #DA7D02;

// 2. Import default variables and available mixins.
@import "../node_modules/uikit/src/scss/variables.scss";
@import "../node_modules/uikit/src/scss/mixins.scss";

// 3. Your custom mixin overwrites.
// @mixin hook-card() { color: #000; }

// 4. Import UIkit.
@import "../node_modules/uikit/src/scss/uikit.scss";
</style>
