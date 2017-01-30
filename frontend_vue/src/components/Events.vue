<template>
  <div id="events" class="container">
    <h1>Events</h1>
    <p>Here are some events.</p>
    <event-cards></event-cards>
  </div>
</template>

<script>
import EventCards from './EventCards';

export default {
  name: 'events',
  data() {
    return {};
  },
  components: {
    EventCards,
  },
};
</script>

<style lang="scss" scoped>
</style>
