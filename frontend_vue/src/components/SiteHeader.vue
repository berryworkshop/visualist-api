<template>
  <header id="site-header" @keyup.esc="close">
    <div class="container"> 
      <div id="masthead">
        <div id="branding">
          <a href="">Visualist</a>
        </div>
      </div>
      <div id="primary_nav">
        <router-link to="/" tabindex="0"><i class="fa fa-home fa-2x" aria-hidden="true"></i></router-link>
        <form id="search" action="/search">
          <input type="search" placeholder="Search" name="q" >
          <button type="submit">
            <i class="fa fa-search" aria-hidden="true"></i>
          </button>
        </form>
        <div id="browse">
          <button type="button" class="browse_modal_toggle" v-on:click="browse_modal = !browse_modal">
            <i class="fa fa-bars fa-2x" aria-hidden="true"></i>
          </button>
        </div>
      </div>
      <div id="browse_modal" v-if="browse_modal">
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
    };
  },
  methods: {
    close() {
      this.browse_modal = false;
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

    #branding {
      font-size: 2rem;
      font-weight: bold;
      flex: auto;

      a {
        color: white;
      }
    }
    
    #menu {
      color: #777;
    }
  }

  #primary_nav {
    background-color: #333;
    width: 100%;
    display: flex;
    flex-direction: row;
    color: #999;
    padding: 1rem;
    margin: 0 -1rem;

    > * {
      margin-right: 1rem;

    }

    > :last-child {
      margin-right: 0;
    }

    > a {
      color: #999
    }

    button {
      color: #999;
      border: none;
    }

    #search {
      display: flex;
      flex: auto;

      input {
        flex: auto;
        padding: .25rem .5rem;
        border: 0;
        background-color: #ddd;
      }
      button {   
        padding: .25rem .5rem;
        background-color: hsla(0,0%,0%,0.5);
      }
    }
    #browse {
      button {   
        padding: 0;
        background-color: transparent;
      }
    }
  } 
    #browse_modal {
      position: absolute;
      top: 100%;
      left: 0;
      right: 0;
      z-index: 1;
      background-color: $secondary_bg;
      padding: 1rem;
      box-shadow: 0 3px 3px hsla(0,0%,0%,0.5);
    }
}
</style>
