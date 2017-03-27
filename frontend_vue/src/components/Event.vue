<template>
  <div class="panel" id="event">
    <p>Name</p>
    <p>Event ID: {{ $route.params.event_id }}</p>
    <p>Description</p>
    <p>Category</p>
  </div>
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
    mounted() {
      this.$store.commit('setPageData', {
        title: 'Event',
        subtitle: '',
        description: '',
      });
      ajax.get(`/events/${this.$route.params.event_id}`)
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        this.error = error;
        console.log(error);
      });
    },
  };
</script>

<style lang="scss" scoped>
</style>
