<template>
  <div id="login" class="container">
    <h1>Login</h1>
    <p>Login to the Visualist.</p>

    <p>{{ msg }}</p>

    <form id="login_form">
      <label for="username">Username</label>
      <input id="username" v-model="username" placeholder="username">

      <label for="password">Password</label>
      <input v-model="password" type="password" placeholder="password">

      <button type="submit" v-on:click="warn('Form cannot be submitted yet.', $event)">
        Login <i class="fa fa-sign-in" aria-hidden="true"></i>
      </button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'login',
  data() {
    return {
      username: '',
      password: '',
      msg: '',
    };
  },
  methods: {
    warn(message, event) {
      if (event) {
        event.preventDefault();
      }
      this.msg = message;
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
