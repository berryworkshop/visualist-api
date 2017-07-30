<template>
  <div class="directory">
    <vis-header></vis-header>
    <h1>Directory</h1>

    <fieldset class="personForm">
      <input type="text"
        id="name_first"
        name="name_first"
        v-model="person.name.first"
        v-on:keyup.enter.prevent="postPerson">
      <label for="name_first">First Name</label>

      <br>

      <input type="text"
        id="name_last"
        name="name_last"
        v-model="person.name.last"
        v-on:keyup.enter.prevent="postPerson"
        required>
      <label for="name_last">Last Name</label>

      <p>{{ slug }}</p>
      <button v-on:click="postPerson">Post</button>
    </fieldset>

    <button v-on:click="deletePeople">Delete People</button>

    <ul v-if="people.length > 0">
      <li
        v-for="p in people"
        :key="p.slug">
        {{ p.name.first }} {{ p.name.last }}
      </li>
    </ul>
  </div>
</template>

<script>
import VisHeader from './_VisHeader.vue';
import axios from 'axios';
import slug from 'slug';

function blankPerson() {
  return {
    name: {
      first: '',
      last: '',
    },
    slug: '',
  }
}

export default {
  name: 'directory',
  components: {
    VisHeader,
  },
  data() {
    return {
      person: blankPerson(),
      people: [],
    };
  },
  created() {
    this.getPeople()
  },
  methods: {
    async getPeople() {
      try {
        const response = await axios.get(`http://localhost:8000/api/v1/people`);
        this.people = response.data._items;
      } catch (e) {
        console.error(e);
      }
    },
    async postPerson() {
      try {
        // make sure the person has a slug
        const person = this.person;
        person['slug'] = this.slug;
        const response = await axios.post(`http://localhost:8000/api/v1/people`, person);
        this.getPeople();
        this.person = blankPerson();
      } catch (e) {
        console.error(e);
      }
    },
    async deletePeople() {
      try {
        const response = await axios.delete(`http://localhost:8000/api/v1/people`);
        this.getPeople();
      } catch (e) {
        console.error(e);
      }
    },
  },
  computed: {
    slug: function () {
      const divider = (this.person.name.first && this.person.name.last) ? '-' : '';
      return slug(`${ this.person.name.last } ${ this.person.name.first }`); 
    }
  }
};
</script>

<style lang="scss" scoped>

</style>
