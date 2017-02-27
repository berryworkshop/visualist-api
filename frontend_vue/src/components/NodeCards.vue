<template>
  <div class="panel">
    <ul class="card_list">
      <li v-for="obj in objectList" class="card">
        <div class="node_visuals">
          <h4 class="node_date_icon">Jan 1 – Jan 30</h4>
        </div>
        <div class="node_info">
          <p class="location">
            <span v-if="obj.city">{{ obj.city }}</span>
            <span v-if="obj.location">: {{ obj.location }}</span>
          </p>
          <h3 class="title">{{ obj.name }}</h3>
          <p class="synopsis">This is the synopsis.  It's limited to 255 characters.  Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisiut.</p>
          <p class="audience">All ages welcome</p><!-- tiered as a vocab -->
          <i class="fa fa-usd" aria-hidden="true"></i>
        </div>
        <div class="node_controls">
          <a class="button" href="#"><i class="fa fa-star" aria-hidden="true"></i></a>
          <a class="button" href="#"><i class="fa fa-flag" aria-hidden="true"></i></a>

          <a class="button" href="#"><i class="fa fa-pencil" aria-hidden="true"></i></a>
          <a class="button" href="#"><i class="fa fa-trash" aria-hidden="true"></i></a>

          <a class="button" href="#"><i class="fa fa-map-marker" aria-hidden="true"></i></a>
          <a class="button" href="#"><i class="fa fa-share" aria-hidden="true"></i></a>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
  import Axios from 'axios';

  const ajax = Axios.create({
    baseURL: process.env.API_BASE_URL,
  });

  export default {
    name: 'node-cards',
    data() {
      return {
        objectList: [],
        error: '',
      };
    },
    mounted() {
      ajax.get('/nodes/')
      .then((response) => {
        this.objectList = response.data._items;
      })
      .catch((error) => {
        console.log(error);
      });
    },
  };

</script>

<style lang="scss">
  @import "../styles/brand.scss";
  @import "../styles/grid.scss";
  @import "../styles/utility.scss";

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
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;

    li {
      margin-bottom: 1rem;
      @include md_up {
        flex: 1 0 45%;
        background-clip: padding-box;
        &:nth-of-type(odd) {
          margin-right: .5rem;
        }
        &:nth-of-type(even) {
          margin-left: .5rem;
        }
      }
    }
  }

  .node_visuals {
    margin-left: -1rem;
    margin-right: -1rem;
    margin-top: -1rem;
    padding: 1rem;
    background-color: silver;
    background: url("http://placehold.it/600x300.png?text=image") center center no-repeat;
    background-size: cover;
    height: 17.5rem;

    > * {
      position: flex;
      flex-direction: column;
      color: white;
    }

    .node_date_icon {
      font-size: x-large;
      font-weight: normal;
      margin: auto;
    }
  }



</style>
