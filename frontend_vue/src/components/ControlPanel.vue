<template>
  <aside id="control-panel">

    <fieldset>
      <legend>Format</legend>
      <input type="radio" name="format" checked> Gallery
      <input type="radio" name="format"> Bento
      <input type="radio" name="format"> Table
      <input type="radio" name="format"> Map
      <input type="radio" name="format"> Timeline
      <input type="radio" name="format"> Calendar
    </fieldset>

    <fieldset>
      <legend>Filters</legend>
      <button name="reset">Reset</button>

      <fieldset>
        <legend>Keyword</legend>
        <input type="text" placeholder="Terms">
      </fieldset>

      <fieldset>
        <legend>Tag</legend>
        <select>
          <option>Aardvarks</option>
          <option>Meerkats</option>
          <option>Zebras</option>
        </select>
      </fieldset>

      <fieldset>
        <legend>Content Type</legend>

        <input type="checkbox" name="datatype" checked> Events
        <fieldset>
          <input type="checkbox" name="event_attr" checked> All Ages
          <input type="checkbox" name="event_attr" checked> Organizations
          <input type="checkbox" name="event_attr" checked> People
        </fieldset>

        <input type="checkbox" name="datatype" checked> Organizations
        <fieldset>
          <input type="checkbox" name="org_attr" checked> Is a Venue
          <input type="checkbox" name="org_attr" checked> Nonprofit
        </fieldset>

        <input type="checkbox" name="datatype" checked> People
        <fieldset>
          <input type="checkbox" name="person_attr" checked> Artist
          <input type="checkbox" name="person_attr" checked> Smells OK
        </fieldset>

        <input type="checkbox" name="datatype" checked> Artworks
        <fieldset>
          <input type="checkbox" name="work_attr" checked> Doesn't Suck
        </fieldset>
      </fieldset>

      <fieldset>
        <legend>Time</legend>
        <input type="checkbox" name="time" checked> Yesterday
        <input type="checkbox" name="time" checked> Today
        <input type="checkbox" name="time" checked> Tomorrow
      </fieldset>

      <fieldset>
        <legend>Location</legend>
        <input type="checkbox" name="location" checked> Nearby
        <input type="checkbox" name="location" checked> Far Away
      </fieldset>
    </fieldset>

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
