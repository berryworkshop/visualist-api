<template>
  <div class="nav-primary">
    <ul>
        <li><router-link :to="{name: 'home'}">Home</router-link></li>
        <li><router-link :to="{name: 'login'}">Login</router-link></li>
        <li><router-link :to="{name: 'people'}">People</router-link></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'login',
};
</script>

<style scoped>

</style>
