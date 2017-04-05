<template>
  <div class="panel" id="list">

    <!-- New Event modal -->
    <a class="uk-button uk-button-default" href="#modal-sections" uk-toggle>New Event</a>
    <div id="modal-sections" uk-modal="center: true">
      <div class="uk-modal-dialog">
        <button class="uk-modal-close-default" type="button" uk-close></button>
        <div class="uk-modal-header">
          <h2 class="uk-modal-title">New Event</h2>
        </div>
        <form method="post" v-on:submit.prevent="submit_form">
          <div class="uk-modal-body">
              <fieldset class="uk-fieldset">

                <!-- <legend class="uk-legend">Flurm</legend> -->

                <div class="uk-margin">
                  <label class="uk-form-label" for="name">Name</label>
                  <input class="uk-input uk-form-large" id="name" v-model="event.name" type="text" placeholder="Event Name">
                </div>

                <div class="uk-margin">
                  <label class="uk-form-label" for="description">Description</label>
                  <textarea class="uk-input" id="description" v-model="event.description" type="textarea" placeholder="Event Description" rows="6"></textarea>
                </div>

                <div class="uk-margin">
                  <label class="uk-form-label" for="category">Category</label>
                  <select class="uk-select" id="category" v-model="event.category">
                      <option value="reception">Reception</option>
                      <option value="exhibition">Exhibition</option>
                  </select>
                </div>

              </fieldset>
          </div>
          <div class="uk-modal-footer uk-text-right">
            <button class="uk-button uk-button-default uk-modal-close" type="button">Cancel</button>
            <button class="uk-button uk-button-primary" type="submit">Save</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Event list -->
    <template v-for="event in events">
      <div class="uk-card uk-card-default uk-grid-collapse uk-child-width-1-2@s uk-margin" uk-grid>
        <div class="uk-card-media-left uk-cover-container">
            <img src="http://placehold.it/600x400" alt="" uk-cover>
            <canvas width="600" height="400"></canvas>
        </div>
        <div>
            <div class="uk-card-body">
                <h3 class="uk-card-title"><router-link :to="{ name: 'event', params: { event_id: event.id }}">
                  {{ event.name }}
                </router-link></h3>
                <p>{{ event.description }}</p>
                <p>{{ event.category }}</p>
            </div>
        </div>
      </div>
    </template>


</div>
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
