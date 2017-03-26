<template>
  <div class="panel" id="eventForm">
    <form method="post" v-on:submit.prevent="onSubmit">
        <fieldset>
            <div class="row">
                <label for="name">Name</label>
                <input class="input" id="name" type="text" placeholder="Event Name" v-model="event.name">
                <span class="feedback">
                    <i class="fa fa-exclamation-circle" aria-hidden="true"></i>
                </span>
            </div>
            <div class="row">
                <label for="description">Description</label>
                <textarea class="input" id="description" type="textarea" placeholder="Event Description" v-model="event.description" rows="5"></textarea>
                <span class="feedback">
                    <i class="fa fa-exclamation-circle" aria-hidden="true"></i>
                </span>
            </div>
            <div class="row">
                <label for="category">Category</label>
                <select class="input" id="category" v-model="event.category">
                    <option value="reception">Reception</option>
                    <option value="exhibition">Exhibition</option>
                </select>
                <span class="feedback">
                    <i class="fa fa-exclamation-circle" aria-hidden="true"></i>
                </span>
            </div>
            <div class="submit_row">
                <a href="">Cancel</a>
                <button type="submit">Submit</button>
            </div>
        </fieldset>
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
            this.$router.go('/nodes');
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
    form {
        fieldset {
            padding: 1rem;
            margin-bottom: 1rem;
            .row {
                display: flex;
                padding-bottom: 1rem;
                label {
                    flex-basis: 6rem;
                    flex-shrink: 0;
                    margin-right: 1rem;
                    text-align: right;
                    padding-top: .5rem;
                    // border: 1px solid red;
                }
                .input {
                    flex: 2 1 20rem;
                    // border: 1px solid green;
                }
                .feedback {
                    flex-basis: 1rem;
                    margin-left: 1rem;
                    // border: 1px solid blue;
                }
            }
            .submit_row {
                text-align: right;
                margin-right: 2rem;
            }
        }
    }
</style>
