<template>
  <main id="event-list">
    <div>
      <h1>List of Events</h1>
    </div>

    <div class="content">
      <form action="post" v-on:submit.prevent="submit_form($event)">
        <input v-model="event.name" placeholder="Name">
        <textarea v-model="event.description" placeholder="Description"></textarea>
        <select v-model="event.category" placeholder="exhibition">
          <option value="exhibition">Exhibition</option>
          <option value="reception">Reception</option>
        </select>
        <button type="submit">Submit</button>
      </form>

      <template v-for="event in events">
        <h3><router-link :to="{ name: 'event', params: { event_id: event.id }}">
          {{ event.name }}
        </router-link></h3>
        <p>{{ event.description }}</p>
        <p>{{ event.category }}</p>
      </template>
    </div>

    <div class="sidebar">
      <p>sidebar</p>
    </div>
  </main>
</template>

<script>
  import Axios from 'axios';

  const ajax = Axios.create({
    baseURL: process.env.API_BASE_URL,
  });

  export default {
    name: 'list',
    data() {
      return {
        show_modal: false,
        events: [],
        event: {},
      };
    },
    created() {
      this.reset_form();
      this.update_events();
    },
    methods: {
      update_events() {
        ajax.get('/events')
        .then((response) => {
          this.events = response.data.events;
        })
        .catch((error) => {
          this.error = error;
          if (error.response.status === 404) {
            this.$router.push({ name: '404' });
          }
          console.log(error);
        });
      },
      submit_form(e) {
        ajax.post('/events', this.event)
        .then((response) => {
          if (response.status === 200) {
            console.log(response);
            console.log(e);
            this.update_events();
            this.reset_form();
          } else {
            console.log(response);
          }
        })
        .catch((error) => {
          this.error = error;
          console.log(error);
        });
        this.update_events();
        // window.UIkit.offcanvas('#modal-sections').toggle();
      },
      reset_form() {
        this.event = {
          name: '',
          description: '',
          category: 'exhibition',
        };
      },
    },
  };
</script>

<style lang="scss" scoped>
  form > * {
    display: block;
  }
</style>
