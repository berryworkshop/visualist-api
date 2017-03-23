<template>
  <aside id="control-panel">
    <fieldset>
      <legend>Format</legend>
      <p>Choose relevant presentation scheme. Default: Cards.</p>
      <input type="radio" name="format" checked> Cards
      <!--<input type="radio" name="format"> Bento-->
      <!--<input type="radio" name="format"> Table-->
      <input type="radio" name="format"> Map
      <!--<input type="radio" name="format"> Timeline-->
      <input type="radio" name="format"> Calendar
    </fieldset>

    <fieldset>
    <legend>Facets</legend>
    <button name="reset">Reset</button>

      <fieldset>
        <legend>Selectors</legend>
        <p>Negative selectors; default to all.  Amazon style?</p>
        <fieldset>
          <legend>Content Types</legend>
          <p>Record categories/labels.</p>
          <input type="checkbox" name="datatype" checked> Events
          <input type="checkbox" name="datatype" checked> Organizations
          <input type="checkbox" name="datatype" checked> People
          <input type="checkbox" name="datatype" checked> Artworks
        </fieldset>

        <!--<fieldset>
          <legend>Properties</legend>
          <p>Record properties/attributes.</p>

          <fieldset>
            <legend>Shared</legend>
            <input type="checkbox" name="shared_attr" checked> 4 stars and up
          </fieldset>

          <fieldset>
            <legend>Events</legend>
            <input type="checkbox" name="event_attr" checked> All Ages
            <input type="checkbox" name="event_attr" checked> Organizations
            <input type="checkbox" name="event_attr" checked> People
          </fieldset>

          <fieldset>
            <legend>Organization</legend>
            <input type="checkbox" name="org_attr" checked> Is a Venue
            <input type="checkbox" name="org_attr" checked> Nonprofit
          </fieldset>

          <fieldset>
            <legend>Person</legend>
            <input type="checkbox" name="person_attr" checked> Artist
            <input type="checkbox" name="person_attr" checked> Smells OK
          </fieldset>

          <fieldset>
            <legend>Artwork</legend>
            <input type="checkbox" name="work_attr" checked> Doesn't Suck
          </fieldset>
        </fieldset>-->
      </fieldset>

      <fieldset>
        <legend>Limiters</legend>
        <p>Positive limiters; default to none.  CCC style.</p>

        <fieldset>
          <legend>Keywords</legend>
          <p>Arbitrary record text.</p>
          <input type="text" placeholder="Terms">
        </fieldset>

        <!--<fieldset>
          <legend>Facets</legend>
          <p>External, hierarchical, controlled vocabularies.</p>

          <fieldset>
            <legend>Events</legend>
            <select multiple>
              <option>Aardvarks</option>
              <option>Meerkats</option>
              <option>Zebras</option>
            </select>
          </fieldset>

          <fieldset>
            <legend>Organizations</legend>
            <select multiple>
              <option>Aardvarks</option>
              <option>Meerkats</option>
              <option>Zebras</option>
            </select>
          </fieldset>

          <fieldset>
            <legend>People</legend>
            <select multiple>
              <option>Aardvarks</option>
              <option>Meerkats</option>
              <option>Zebras</option>
            </select>
          </fieldset>

          <fieldset>
            <legend>Artworks</legend>
            <select multiple>
              <option>Aardvarks</option>
              <option>Meerkats</option>
              <option>Zebras</option>
            </select>
          </fieldset>
        </fieldset>-->

        <fieldset>
          <legend>Tags</legend>
          <p>Unstructured, user-submitted tags.</p>

          <select multiple>
            <option>Aardvarks</option>
            <option>Meerkats</option>
            <option>Zebras</option>
          </select>
        </fieldset>

        <fieldset>
          <legend>Date</legend>
          <p>Time span.</p>
          <input type="checkbox" name="date"> Yesterday
          <input type="checkbox" name="date"> Today
          <input type="checkbox" name="date"> Tomorrow
          <input type="checkbox" name="date"> This Week
          <input type="checkbox" name="date"> This Month
        </fieldset>

        <fieldset>
          <legend>Location</legend>
          <p>Geographic area.</p>
          <input type="checkbox" name="location"> Country
          <input type="checkbox" name="location"> Far Away
        </fieldset>

        <!--<fieldset>
          <legend>Image</legend>
          <p>Image analysis.</p>

          <select multiple>
            <option>green</option>
            <option>blue</option>
            <option>red</option>
            <option>people in image</option>
          </select>
        </fieldset>-->

        <!--<fieldset>
          <legend>NLP</legend>
          <p>Natural language matching.</p>

          <select multiple>
            <option>reading level</option>
            <option>hrm</option>
          </select>
        </fieldset>-->

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
