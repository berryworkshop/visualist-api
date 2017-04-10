<template>
  <main id="event-list">
    <div>
      <h1>List of Events</h1>
    </div>

    <div class="content">
      <form action="post" v-on:submit.prevent="form_submit">
        <input v-model="event.name" placeholder="Name">
        <textarea v-model="event.description" placeholder="Description"></textarea>
        <select v-model="event.category" placeholder="exhibition">
          <option value="exhibition">Exhibition</option>
          <option value="reception">Reception</option>
        </select>
        <button type="submit">Submit</button>
      </form>

      <template v-for="event in events">
        <input type="checkbox" v-model="event.selected">
        <button v-on:click="event_delete(event.id)">Delete</button>
        <h3><router-link :to="{ name: 'event', params: { event_id: event.id }}">
          {{ event.name }}
        </router-link></h3>
        <p>{{ event.id }}</p>
        <p>{{ event.description }}</p>
        <p>{{ event.category }}</p>
        <p>{{ event.selected }}</p>
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
      this.form_reset();
      this.events_update();
      this.events_selected_clear();
    },
    methods: {
      events_update() {
        ajax.get('/events')
        .then((response) => {
          // check if events have a selected prop; if not, then oblige
          for (const e of response.data.events) {
            if (!Object.prototype.hasOwnProperty.call(e, 'selected')) {
              e.selected = false;
            }
          }
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
      form_submit() {
        ajax.post('/events', this.event)
        .then((response) => {
          if (response.status === 200) {
            console.log(response);
            this.events_update();
            this.form_reset();
          } else {
            console.log(response);
          }
        })
        .catch((error) => {
          this.error = error;
          console.log(error);
        });
        this.events_update();
        // window.UIkit.offcanvas('#modal-sections').toggle();
      },
      form_reset() {
        this.event = {
          id: '',
          name: '',
          description: '',
          category: 'exhibition',
        };
      },
      events_selected_clear() {
        for (const event of this.events) {
          event.selected = false;
        }
      },
      event_delete(eventId) {
        console.log(`event #${eventId} deleted`);
        ajax.delete(`/events/${eventId}`)
        .then((response) => {
          if (response.status === 200) {
            console.log(response);
            this.events_update();
          } else {
            console.log(response);
          }
        })
        .catch((error) => {
          this.error = error;
          console.log(error);
        });
      },
    },
  };
</script>

<style lang="scss" scoped>
  form > * {
    display: block;
  }
</style>
