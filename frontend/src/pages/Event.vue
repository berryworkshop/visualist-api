<template>
  <main id="event">
    <h1>{{ event.name }}</h1>
    <p>Event ID: {{ $route.params.event_id }}</p>
    <p>Description: {{ event.description }}</p>
    <p>Category: {{ event.category }}</p>
  </main>
</template>

<script>
  import Axios from 'axios';

  const ajax = Axios.create({
    baseURL: process.env.API_BASE_URL,
  });

  export default {
    name: 'event',
    data() {
      return {
        event: {
          name: '',
          description: '',
          category: '',
        },
        error: '',
      };
    },
    created() {
      ajax.get(`/events/${this.$route.params.event_id}`)
      .then((response) => {
        this.event = response.data.event;
      })
      .catch((error) => {
        this.error = error;
        if (error.response.status === 404) {
          this.$router.push({ name: '404' });
        }
        console.log(error);
      });
    },
  };
</script>

<style lang="scss" scoped>
</style>
