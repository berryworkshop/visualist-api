<template>
  <div class="card-event">
    <header class="card-header">
      <input type="checkbox" v-model="selected">
    </header>
    <div class="card-main">
      <h3>
        <router-link :to="{ name: 'event', params: { event_id: id }}">{{ name }}</router-link>
      </h3>
      <dl>
        <dt>id</dt><dd>{{ id }}</dd>
        <dt>description</dt><dd>{{ description }}</dd>
        <dt>category</dt><dd>{{ category }}</dd>
      </dl>
    </div>
    <footer class="card-footer">
      <button v-on:click="delete_event">Delete</button>
    </footer>
  </div>
</template>


<script>
  import Axios from 'axios';

  const ajax = Axios.create({
    baseURL: process.env.API_BASE_URL,
  });

  export default {
    name: 'card-event',
    props: [
      'event',
    ],
    data() {
      return {
        id: this.event.id,
        name: this.event.name,
        description: this.event.description,
        category: this.event.category,
        selected: this.event.selected,
      };
    },
    methods: {
      delete_event() {
        ajax.delete(`/events/${this.id}`)
        .then((response) => {
          if (response.status === 200) {
            console.log(`event #${this.id} deleted`);
            this.$emit('remove');
            // console.log(response);
            // this.events_update();
          } else {
            console.error(`event #${this.id} failed to delete`);
            console.error(response);
          }
        })
        .catch((error) => {
          this.error = error;
          console.error(error);
        });
      },
    },
  };
</script>

<style lang="scss" scoped>
  .card-event {
    border: 1px solid silver;
    margin-bottom: .5rem;

    header.card-header {
      padding: 1rem;
      background: url("http://loremflickr.com/g/600/800/chicago") no-repeat center center;
      background-size: cover;
      height: 12rem;
    }
    div.card-main {
      padding: 1rem;
    }
    footer.card-footer {
      text-align: right;
    }
  }
</style>
