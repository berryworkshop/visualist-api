<template>
  <div id="app">
    <site-header></site-header>
    <main>
      <router-view></router-view>
    </main>
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
  // Import Bulma's initial variables
  @import "../node_modules/bulma/sass/utilities/_all.sass";
  // Override initial variables here
  // You can add new ones or update existing ones:

  $blue: #72d0eb; // Update blue
  $pink: #ffb3b3; // Add pink
  $family-serif: "Georgia", serif; // Add a serif family

  // Override generated variables here
  // For example, by default, the $danger color is $red and the font is sans-serif
  // You can change these values:

  $danger: $orange; // Use the existing orange
  $family-primary: $family-serif; // Use the new serif family

  @import "../node_modules/bulma/bulma";
</style>
