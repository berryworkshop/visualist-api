<template>
  <div class="panel" id="event">
    <h1>{{ event.name }}</h1>
    <p>Event ID: {{ $route.params.event_id }}</p>
    <p>Description: {{ event.description }}</p>
    <p>Category: {{ event.category }}</p>

    <!-- Edit Event modal -->
    <a class="uk-button uk-button-default" href="#modal-sections" uk-toggle>Edit Event</a>
    <div id="modal-sections" uk-modal="center: true">
        <div class="uk-modal-dialog">
            <button class="uk-modal-close-default" type="button" uk-close></button>
            <div class="uk-modal-header">
                <h2 class="uk-modal-title">Edit Event</h2>
            </div>
            <div class="uk-modal-body">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            </div>
            <div class="uk-modal-footer uk-text-right">
                <button class="uk-button uk-button-default uk-modal-close" type="button">Cancel</button>
                <button class="uk-button uk-button-primary" type="button">Save</button>
            </div>
        </div>
    </div>

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
