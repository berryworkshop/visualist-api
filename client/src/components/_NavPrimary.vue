<template>
  <div class="nav-primary">
    <ul>
        <li><router-link :to="{name: 'home'}">Home</router-link></li>
        <li><router-link :to="{name: 'calendar'}">Calendar</router-link></li>
        <li><router-link :to="{name: 'directory'}">Directory</router-link></li>
        <li><router-link :to="{name: 'map'}">Map</router-link></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'nav-primary',
};
</script>

<style scoped>

</style>
