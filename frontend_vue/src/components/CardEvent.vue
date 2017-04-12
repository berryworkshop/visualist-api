<template>
  <div class="card-event">
    <input type="checkbox" v-model="selected">
    <h3><router-link :to="{ name: 'event', params: { event_id: id }}">
      {{ name }}
    </router-link></h3>
    <p>{{ id }}</p>
    <p>{{ description }}</p>
    <p>{{ category }}</p>
    <p>{{ selected }}</p>
    <button v-on:click="delete_event">Delete</button>
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
    padding-left: 1rem;
    padding-right: 1rem;
    margin-bottom: .5rem;

  }
</style>
