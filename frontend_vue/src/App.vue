<template>
  <div id="app">
    <site-header></site-header>

    <main class="container">
      <div id="intro">
        <h1>{{ pageTitle }}</h1>
        <h2 v-if="pageSubtitle">{{ pageSubtitle }}</h2>
        <p v-if="pageDescription">{{ pageDescription }}</p>
      </div>
      <div id="content">
        <router-view></router-view>
      </div>
      <aside id="controls">
        <control-panel></control-panel>
      </aside>
    </main>

    <site-footer></site-footer>
  </div>
</template>


<script>
import { mapState } from 'vuex';
import SiteHeader from './components/SiteHeader';
import ControlPanel from './components/ControlPanel';
import SiteFooter from './components/SiteFooter';

export default {
  name: 'app',
  data() {
    return {};
  },
  components: {
    SiteHeader,
    ControlPanel,
    SiteFooter,
  },
  props: [],
  computed: mapState({
    pageTitle: state => state.page.title,
    pageSubtitle: state => state.page.subtitle,
    pageDescription: state => state.page.description,
  }),
};
</script>


<style lang="scss">
  @import "styles/brand.scss";
  @import "styles/grid.scss";
  @import "styles/utility.scss";

  * { box-sizing: border-box }

  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;

    background-color: $primary_bg;
    color: $primary_text;
    display: flex;
    min-height: 100vh;
    flex-direction: column;
    flex-wrap: wrap;

    .container {
      position: relative;
      margin: 0;
      padding-right: 1rem;
      padding-left: 1rem;

      @include lg_up {
        width: 100%;
        margin-left: auto;
        margin-right: auto;
        max-width: $bp2;
      }
    }

    main {
      flex: 1 0 100%;
      font-size: 16;
      background-color: $primary_bg;
      display: flex;
      flex-direction: column;
      flex-wrap: wrap;
      #intro {
        order: 1;
        flex: 2 1 50%;
      }
      #content {
        order: 3;
      }
      #controls {
        order: 2;
        flex: 1 0;
        display: flex;
        align-items: flex-end;
        padding-bottom: 1rem;
      }
    }

    a {
      color: $primary_anchor;
      font-weight: bolder;
    }

    a.disabled {
      color: $button_text_disabled;
      pointer-events: none;
      cursor: default;
    }

    %form_base {
      background-color: white;
      padding: .5em .75em;
      margin: 0;
      border: 1px solid silver;
    }

    input {
      @extend %form_base;
    }

    select {
      @extend %form_base;
    }

    // abstract superclass for "button-like" things, like block anchors, tabs, etc.
    %button_base {
      @extend %form_base;
      color: $button_text;
      background-color: $button_bg;

      text-decoration: none;
      cursor: pointer;

      &:hover {
        background-color: $button_bg_hover;
      }
      &:active {
        background-color: $button_bg_active;
      }
    }

    button {
      @extend %button_base;
      color: $button_text;
    }

    // tab group, consisting of linked anchors
    ul.tab_list {
      display: flex;
      margin: 0;
      padding: 0;
      list-style-type: none;

      li {
        margin-right: .25rem;
        &:last-child {
          margin-right: 0;
        }
        a {
          @extend %button_base;
          font-size: 20px;
          display: block;
          padding: 1em 1em 1rem 1em;
          border-bottom-width: 0;
        }
      }
    }

    control-panel {
      border: 1px solid red;
    }
  }
</style>
