<template>
  <main id="list" class="container">
    <!-- Event list -->
    <template v-for="event in events">
        <h3><router-link :to="{ name: 'event', params: { event_id: event.id }}">
          {{ event.name }}
        </router-link></h3>
        <p>{{ event.description }}</p>
        <p>{{ event.category }}</p>
    </template>
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
        event: { // New event
          name: '',
          description: '',
          category: '',
        },
      };
    },
    created() {
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
      submit_form() {
        ajax.post('/events', this.event)
        .then((response) => {
          if (response.status === 200) {
            this.$router.push({ name: 'events' });
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
    },
  };
</script>

<style lang="scss" scoped>
</style>
