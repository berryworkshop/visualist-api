var EventCards = require('./event_cards.vue')
Vue.component('event_cards', EventCards)

var home = new Vue({
    delimiters: ['[{', '}]'],
    el: 'main',
    data: {
        events: [],
        components: [
            EventCards
        ]
    }
})

var mymap = L.map('mapid').setView([41.8781, -87.6298], 13);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/cit4vck8m001v2wrpq6lhhcfk/tiles/256/{z}/{x}/{y}?access_token={accessToken}', {
    id: 'aljabear',
    accessToken: 'pk.eyJ1IjoiYWxqYWJlYXIiLCJhIjoiY2l0NHJtM3plMDAwMjJ6bzM4Y3M2Z201biJ9.HvF_jJ4TnzYXle8uL5XhtQ'
}).addTo(mymap);