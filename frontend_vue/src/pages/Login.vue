<template>
  <main id="login">
    <h1>Login</h1>
    <p>Login to the Visualist.</p>

    <p>{{ msg }}</p>

    <form id="login_form">
      <table>
        <tr>
          <th><label for="username">Username</label></th>
          <td><input id="username" v-model="username" placeholder="username"></td>
        </tr>
        <tr>
          <th><label for="password">Password</label></th>
          <td><input v-model="password" type="password" placeholder="password"></td>
        </tr>
        <tr>
          <td></td>
          <td>
            <button type="submit" v-on:click="warn('Form cannot be submitted yet.', $event)">
              Login <i class="fa fa-sign-in" aria-hidden="true"></i>
            </button>
          </td>
        </tr>
      </table>
    </form>
  </main>
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
