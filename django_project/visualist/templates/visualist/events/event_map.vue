<template>
    <div class="panel">
        <div id="leaflet_map"></div>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.0-rc.3/dist/leaflet.css" />
    </div>
</template>

<script>
    require('leaflet');

    export default {
        name: 'event_map',
        data() {
            return {}
        },
        mounted: function() {
            var mymap = L.map('leaflet_map').setView([41.8781, -87.6298], 13);
            L.tileLayer('https://api.mapbox.com/styles/v1/{id}/cit4vck8m001v2wrpq6lhhcfk/tiles/256/{z}/{x}/{y}?access_token={accessToken}', {
                id: 'aljabear',
                accessToken: 'pk.eyJ1IjoiYWxqYWJlYXIiLCJhIjoiY2l0NHJtM3plMDAwMjJ6bzM4Y3M2Z201biJ9.HvF_jJ4TnzYXle8uL5XhtQ'
            }).addTo(mymap);
        }
    }
</script>

<style lang="sass"></style>