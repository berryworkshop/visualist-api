<template>
  <div id="app">
    <div class="ribbon secondary">
      <site-header class="container"></site-header>
    </div>
    <div class="ribbon">
      <site-main class="container"></site-main>
    </div>
    <div class="ribbon secondary">
      <site-footer class="container"></site-footer>
    </div>
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
  @import "main.scss";

  // breakpoints
  // https://medium.freecodecamp.com/the-100-correct-way-to-do-css-breakpoints-88d6a5ba1862
  @mixin for_phone_only {
    @media (max-width: 599px) { @content; }
  }
  @mixin for_tablet_portrait_up {
    @media (min-width: 600px) { @content; }
  }
  @mixin for_tablet_landscape_up {
    @media (min-width: 900px) { @content; }
  }
  @mixin for_tablet_landscape_down {
    @media (max-width: 1199px) { @content; }
  }
  @mixin for_desktop_up {
    @media (min-width: 1200px) { @content; }
  }
  @mixin for_desktop_only {
    @media (min-width: 1200px) { @content; }
    @media (max-width: 1799px) { @content; }
  }
  @mixin for_big_desktop_up {
    @media (min-width: 1800px) { @content; }
  }

  // ribbon only at this level
  .ribbon {
    width: 100%;
    &.secondary {
      color: white;
      background-color: $color-secondary;
      a:focus, a:hover {
        color: $color-primary-light;
      }
      a:focus {
        color: $color-primary-dark;
      }
    }
  }

  // containers used within site sections, for page width/device responsiveness
  .container {

    // phones and tablets get some edge padding
    @include for_tablet_landscape_down {
      padding-left: 1rem;
      padding-right: 1rem;
    }

    // page centers for desktop
    @include for_tablet_landscape_up {
      max-width: 900px;
      margin-left: auto;
      margin-right: auto;
    }

    // sub containers should never have L/R margins
    .container {
      margin: inherit 0 !important;
    }
  }

</style>
