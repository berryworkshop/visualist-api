<template>
  <layout-default>
    <h2>Calendar</h2>

    <section id="events">
      <h3>Records</h3>
      <ul>
        <li v-for="record in records"
            :key="record.slug">
          <div class="record" id="record.slug">
            <h4>{{ record.label }}: {{ record.slug }}</h4>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam veniam libero in! Laborum in corrupti alias reprehenderit cumque enim, fugiat velit dolorum, nobis maxime ea veniam. Nam ducimus accusantium aliquam.</p>
          </div>
        </li>
      </ul>
    </section>
  </layout-default>
</template>

<script>
import req from 'superagent';
import LayoutDefault from './layouts/Default';

export default {
  name: 'calendar',
  components: {
    LayoutDefault,
  },
  data() {
    return {
      records: [],
    };
  },
  async created() {
    try {
      let apiRoot = '';
      if (process.env.NODE_ENV === 'development') {
        apiRoot = 'http://localhost:8000';
      }
      const res = await req.get(`${apiRoot}/api/records.json`);
      this.records = res.body.results;
    } catch (err) {
      console.error(err); // eslint-disable-line no-console
    }
  },
};
</script>


<style lang='scss' scoped>

</style>
