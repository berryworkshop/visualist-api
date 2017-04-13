<template>
  <main id="event-list">
    <h1>List of Events</h1>
    <div class="content">
      <form action="post" v-on:submit.prevent="form_submit">
        <fieldset>
          <legend>New Event</legend>
            <input v-model="event.name" placeholder="Name" type="text">
            <textarea v-model="event.description" placeholder="Description"></textarea>
            <select v-model="event.category" placeholder="exhibition" type="text">
              <option value="exhibition">Exhibition</option>
              <option value="reception">Reception</option>
            </select>
            <button type="submit">Submit</button>
        </fieldset>
      </form>
      <div class="grid">
        <card-event
          v-for="(event, index) in events"
          :event="event"
          :index="index"
          :key="event.id"
          v-on:remove="events.splice(index, 1)"
        ></card-event>
      </div>
    </div>
    <div class="sidebar">
      <p>sidebar</p>
    </div>
  </main>
</template>

<script>
  import Axios from 'axios';
  import CardEvent from '../components/CardEvent';

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
      // this.events_selected_clear();
    },
    components: {
      CardEvent,
    },
    methods: {
      events_update() {
        ajax.get('/events')
        .then((response) => {
          // check if events have a selected prop; if not, then oblige
          for (const evt of response.data.events) {
            if (!Object.prototype.hasOwnProperty.call(evt, 'selected')) {
              evt.selected = false;
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
      },
      form_reset() {
        this.event = {
          id: '',
          name: '',
          description: '',
          category: 'exhibition',
        };
      },
    },
  };
</script>

<style lang="scss" scoped>

  .grid {
    display: flex;
    flex-wrap: wrap;

    margin-left: -.5rem;
    margin-right: -.5rem;

    & > div {
      flex: 0 1 50%;
    }
  }
</style>
