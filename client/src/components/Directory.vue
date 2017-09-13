<template>
  <div class="hello">
    <h2 class="page_title">Directory</h2>
    <ul v-if="people">
      <li
        v-for="person in people"
        :key="person.slug">{{ person.title }}</li>
    </ul>
  </div>
</template>

<script>
import request from 'superagent';

export default {
  name: 'directory',
  data() {
    return {
      people: [],
    };
  },
  async created() {
    try {
      let apiRoot = '';
      if (process.env.NODE_ENV === 'development') {
        apiRoot = 'http://localhost:8000';
      }

      const res = await request
        .get(`${apiRoot}/api/records/?format=json`);

      this.people = res.body.results;
    } catch (err) {
      console.error(err); // eslint-disable-line no-console
    }
  },
};
</script>

<style scoped>
  .page_title {
    color: green;
  }
</style>
