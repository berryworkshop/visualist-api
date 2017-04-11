<template>
  <div class="card-list">
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

    <ul>
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
</style>
