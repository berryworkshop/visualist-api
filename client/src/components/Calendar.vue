<template>
  <layout-default>
    <h2>Calendar</h2>

    <section id="events">
      <h3>Events</h3>
      <ul>
        <li
          v-for="event in events"
          :key="event.slug">
          <card-record :data="event" :id="event.slug">
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Accusantium, cumque dolorum nulla veniam error sapiente architecto modi rem soluta voluptatem velit maxime pariatur. Labore est quos ab nemo atque beatae!</p>
          </card-record>
        </li>
      </ul>
    </section>
  </layout-default>
</template>

<script>
import req from 'superagent';
import LayoutDefault from './layouts/Default';
import CardRecord from './common/CardRecord';

export default {
  name: 'calendar',
  components: {
    LayoutDefault,
    CardRecord,
  },
  data() {
    return {
      events: [],
    };
  },
  async created() {
    try {
      let apiRoot = '';
      if (process.env.NODE_ENV === 'development') {
        apiRoot = 'http://localhost:8000';
      }
      const res = await req.get(`${apiRoot}/api/events.json`);
      this.events = res.body.results;
    } catch (err) {
      console.error(err); // eslint-disable-line no-console
    }
  },
};
</script>


<style lang='scss' scoped>

// this is duplicate in Directory and Map: DRY up
$gutter: 1rem;

ul {
  padding-left: 0;
  list-style-type: none;

  display: flex;
  flex-wrap: wrap;
  margin: -.5 * $gutter;

  li {
    flex: 0 0 18rem;
    margin: .5 * $gutter;
  }
}

</style>
