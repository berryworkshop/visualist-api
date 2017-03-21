<template>
  <aside id="control-panel">
    <select>
      <option value="events">Events</option>
      <option value="organizations">Organizations</option>
      <option value="people">People</option>
      <option value="works">Artworks</option>
      <option value="all">All</option>
    </select>

    <select multiple>
      <option value="list">List</option>
      <option value="map">Map</option>
    </select>

    <button name="new">New</button>
  </aside>
</template>

<script>
export default {
  name: 'control-panel',
  data() {
    return {
      response: '',
    };
  },
};
</script>

<style lang="scss" scoped>
@import "../styles/brand.scss";

#control-panel {}

</style>
