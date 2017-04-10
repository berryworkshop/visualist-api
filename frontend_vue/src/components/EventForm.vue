<template>
  <div id="event-new">
    <form>
      <p>Form</p>
    </form>
  </div>
</template>

<script>
  import Axios from 'axios';

  const ajax = Axios.create({
    baseURL: process.env.API_BASE_URL,
  });

  export default {
    name: 'event-form',
    data() {
      return {
        event: {
          name: '',
          description: '',
          category: 'reception',
        },
        error: '',
      };
    },
    mounted() {
      this.$store.commit('setPageData', {
        title: 'New Event',
        subtitle: '',
        description: 'Create a new event.',
      });
    },
    methods: {
      onSubmit() {
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
      },
    },
  };
</script>

<style lang="scss" scoped>
</style>
