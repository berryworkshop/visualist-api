<template>
  <aside id="control-panel">
    <select>
      <option value="events">Events</option>
      <option value="organizations">Organizations</option>
      <option value="people">People</option>
      <option value="works">Artworks</option>
      <option value="all">All</option>
    </select>
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
  props: [
    {
      name: 'set-page-title',
      type: Function,
      required: true,
    },
  ],
};
</script>

<style lang="scss" scoped>
@import "../styles/brand.scss";

#control-panel {}

</style>
