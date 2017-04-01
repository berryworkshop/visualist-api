<template>
  <div class="panel" id="card-list">
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
      <p>Cards</p>
    </ul>
  </div>
</template>

<script>
  import Axios from 'axios';

  const ajax = Axios.create({
    baseURL: process.env.API_BASE_URL,
  });

  export default {
    name: 'card-list',
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
        this.error = error;
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
</style>
