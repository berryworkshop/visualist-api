<template>
  <header id="site-header" @keyup.esc="close">
    <div class="container">
      <div id="masthead">
        <div id="branding">
          <router-link to="/" tabindex="0">Visualist</router-link>
        </div>
        <button type="button" class="search_modal_toggle" v-on:click="search_modal = !search_modal">
          <i class="fa fa-search fa-2x" aria-hidden="true"></i>
        </button>
        <button type="button" class="browse_modal_toggle" v-on:click="browse_modal = !browse_modal">
          <i class="fa fa-hand-o-up fa-2x" aria-hidden="true"></i>
        </button>
      </div>

      <div id="search_modal" class="dropdown_modal" v-if="search_modal">
        <form id="search" action="/search">
          <input type="search" placeholder="Search" name="q" >
          <button type="submit">Search</button>
        </form>
      </div>

      <div id="browse_modal" class="dropdown_modal" v-if="browse_modal">
        <ul>
          <li><router-link @click.native="close" to="login">Login</router-link></li>
        </ul>
        <ul>
          <li><router-link @click.native="close" to="/events">Events</router-link></li>
          <li><router-link @click.native="close" to="/venues">Venues</router-link></li>
          <li><router-link @click.native="close" to="/artists">Artists</router-link></li>
          <li><router-link @click.native="close" to="/artworks">Artworks</router-link></li>
        </ul>
        <ul>
          <li>Cities</li>
          <li>Neighborhoods/Communities</li>
        </ul>
        <ul>
          <li>User</li>
          <li>About Us</li>
        </ul>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'site-header',
  data() {
    return {
      browse_modal: false,
      search_modal: false,
    };
  },
  methods: {
    close() {
      this.browse_modal = false;
      this.search_modal = false;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../styles/brand.scss";

header#site-header {
  position: relative;
  background-color: $secondary_bg;
  color: $secondary_text;
  display: flex;
  flex-direction: column;
  a {
    text-decoration: none;
    color: $secondary_anchor;
  }
  #masthead {
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 1rem 0;
    a, i {
      color: white;
    }
    #branding {
      font-size: 2rem;
      font-weight: bold;
      flex: auto;
    }
    button {
      color: #999;
      border: none;
      background-color: $secondary_bg;
      &:focus {
        z-index: 2;
      }
    }
  }
  .dropdown_modal {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    z-index: 1;
    background-color: $secondary_bg;
    padding: 1rem;
    box-shadow: 0 3px 3px hsla(0,0%,0%,0.5);
  }
  #search_modal {}
  #browse_modal {}
}
</style>
