<template>
  <layout-default>
    <h2>Map</h2>

    <div style="height: 20rem">
      <v-map :zoom=11 :center="[41.836944, -87.684722]">
        <v-tilelayer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></v-tilelayer>
        <!-- <v-marker :icon="icon" :lat-lng="[41.836944, -87.684722]"></v-marker> -->
      </v-map>
    </div>

    <section id="places">
      <h3>Places</h3>
      <ul>
        <li
          v-for="place in places"
          :key="place.slug">
          <card-record :data="place" :id="place.slug">
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Accusantium, cumque dolorum nulla veniam error sapiente architecto modi rem soluta voluptatem velit maxime pariatur. Labore est quos ab nemo atque beatae!</p>
          </card-record>
        </li>
      </ul>
    </section>
  </layout-default>
</template>

<script>
import req from 'superagent';
import Leaflet from 'vue2-leaflet';
import LayoutDefault from './layouts/Default';
import CardRecord from './common/CardRecord';

// import icon from '../assets/ic_place_black_24dp/web/ic_place_black_24dp_2x.png';


export default {
  name: 'map',
  components: {
    LayoutDefault,
    CardRecord,
    'v-map': Leaflet.Map,
    'v-tilelayer': Leaflet.TileLayer,
    'v-marker': Leaflet.Marker,
  },
  data() {
    return {
      places: [],
    };
  },
  // computed: {
  //   icon() {
  //     return icon;
  //   },
  // },
  async created() {
    try {
      let apiRoot = '';
      if (process.env.NODE_ENV === 'development') {
        apiRoot = 'http://localhost:8000';
      }
      const res = await req.get(`${apiRoot}/api/places.json`);
      this.places = res.body.results;
    } catch (err) {
      console.error(err); // eslint-disable-line no-console
    }
  },
};
</script>

<style lang='scss' scoped>
@import "~leaflet/dist/leaflet.css";

// this is duplicate in Directory and Calendar: DRY up
$gutter: 1rem;

ul {
  padding-left: 0;
  list-style-type: none;

  display: flex;
  flex-wrap: wrap;
  margin: -.5 * $gutter;

  li {
    flex: 1 0 18rem;
    margin: .5 * $gutter;
  }
}

</style>
