<template>
  <div class="panel" id="nodeList">
    <p>Events, Organizations, People, and Artworks</p>

    <fieldset>
      <legend>Crud</legend>
      <button>New</button>
      <span class="inline_input_group">
        <div class="add_on">
          <input type="checkbox">
        </div>
        <select>
          <option>Edit</option>
          <option>Delete</option>
        </select>
        <button>Go</button>
      </span>
    </fieldset>

    <fieldset>
      <legend>Sort</legend>
      <select>
        <option>Name</option>
        <option>Date</option>
        <option>Distance</option>
      </select>
    </fieldset>

    <ul class="cardList">
      <li v-for="obj in objectList" class="card">
        <div class="nodeVisuals">
          <h4 class="nodeDateIcon">Jan 1 – Jan 30</h4>
        </div>
        <div class="nodeInfo">
          <p class="location">
            <span v-if="obj.city">{{ obj.city }}</span>
            <span v-if="obj.location">: {{ obj.location }}</span>
          </p>
          <h3 class="title">{{ obj.name }}</h3>
          <p class="synopsis">{{ obj.description }}</p>
          <p class="audience">All ages welcome</p><!-- tiered as a vocab -->
          <i class="fa fa-usd" aria-hidden="true"></i>
        </div>
        <div class="nodeControls">
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
      this.$store.commit('setPageData', {
        title: 'Search Results',
        subtitle: '',
        description: '',
      });
      ajax.get('/events')
      .then((response) => {
        this.objectList = response.data.events;
      })
      .catch((error) => {
        console.log(error);
      });
    },
  };

</script>

<style lang="scss">
  @import "../styles/brand.scss";
  @import "../styles/forms.scss";
  @import "../styles/grid.scss";
  @import "../styles/utility.scss";


  .inline_input_group {
    display: inline-flex;
    vertical-align: top;
    div.add_on {
      border: 1px solid silver;
      border-right: none;
      padding: .25em .5em;
      display: flex;
      input {
        align-self: center;
        // bottom: .0625em;
      }
    }
    select {
      border-right: none;
    }
    button {}
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
    padding: 1rem;

    .header {}
    .body {}
    .footer{}
  }

  // supporting container for cards
  ul.cardList {
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

  .nodeVisuals {
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

    .nodeDateIcon {
      font-size: x-large;
      font-weight: normal;
      margin: auto;
    }
  }



</style>
