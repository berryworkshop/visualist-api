<template>
  <layout-default>
    <h2>Directory</h2>

    <section id="events">
      <h3>People and Organizations</h3>
      <ul>
        <li v-for="entity in entities" :key="entity.slug">
          <card-record :data="entity" :id="entity.slug"></card-record>
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
  name: 'directory',
  components: {
    LayoutDefault,
    CardRecord,
  },
  data() {
    return {
      entities: [],
    };
  },
  async created() {
    try {
      let apiRoot = '';
      if (process.env.NODE_ENV === 'development') {
        apiRoot = 'http://localhost:8000';
      }
      const res = await req.get(`${apiRoot}/api/entities.json`);
      this.entities = res.body.results;
    } catch (err) {
      console.error(err); // eslint-disable-line no-console
    }
  },
};
</script>

<style lang='scss' scoped>

// this is duplicate in calendar: DRY up
$gutter: 1rem;

ul {
  padding-left: 0;
  list-style-type: none;

  display: flex;
  flex-wrap: wrap;
  margin: -.5 * $gutter;

  li {
    flex: 1 0 18rem;
    margin: .5 * $gutter;
  }
}

</style>
