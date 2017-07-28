<template>
  <div class="nav-secondary">
    <ul>
        <li><router-link :to="{name: 'login'}">Login</router-link></li>
        <li><router-link :to="{name: 'profile'}">Profile</router-link></li>
        <li><router-link :to="{name: 'search'}">Search</router-link></li>
        <li><router-link :to="{name: 'sitemap'}">Sitemap</router-link></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'nav-secondary',
};
</script>

<style scoped>

</style>
