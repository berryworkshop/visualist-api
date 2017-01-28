<template>
  <div id="app">
    <site-header></site-header>

    <main>
      <div class="container">
        <h1>Home</h1>
        <ul>
            <li><a>Events</a></li>
        </ul>
      </div>
    </main>

    <site-footer></site-footer>
  </div>
</template>

<script>
import SiteHeader from './components/SiteHeader';
import SiteFooter from './components/SiteFooter';

export default {
  name: 'app',
  components: {
    SiteHeader,
    SiteFooter,
  },
};
</script>

<style lang="scss">
@import "styles/brand.scss";
@import "styles/grid.scss";
@import "styles/utility.scss";

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  background-color: $primary_bg;
  color: $primary_text;
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  box-sizing: border-box;

  .container {
    position: relative;
    margin: 0;
    padding-right: 1rem;
    padding-left: 1rem;
    box-sizing: border-box;

    @include lg_up {
      width: 100%;
      margin-left: auto;
      margin-right: auto;
      max-width: $bp2;
    }
  }

  main {
    font-size: 16;
    flex: 1;
    background-color: $primary_bg;
  }

  a {
    color: $primary_anchor;
  }

  a.disabled {
    color: $button_text_disabled;
    pointer-events: none;
    cursor: default;
  }

  // abstract superclass for "button-like" things, like block anchors, tabs, etc.
  %button_base {
    color: $button_text;
    background-color: $button_bg;

    padding: .5em .75em;
    margin: 0;
    border: 1px solid silver;
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

  // abstract superclass for panel and card
  %block {
    display: flex;
    flex-direction: column;
  }

  // good for interface items like control panels and maps
  // can be used to contain cards, or be used within cards
  .panel {
    @extend %block;
    margin: 0;
    padding: 0;
  }

  // good for information presentation like Records, lists, or other items from the database
  // not meant to be self nested
  .card {
    @extend %block;
    background-color: $card_bg;
    margin: 0 0 1rem 0;
    padding: 1rem;

    .header {}
    .body {}
    .footer{}
  }

  // supporting container for cards
  ul.card_list {
    margin: 0;
    padding: 0;
    list-style-type: none;

    display: inline-block;
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
}
</style>
