var EventControls = require('./event_controls.vue')
Vue.component('event_controls', EventControls)

var EventCards = require('./event_cards.vue')
Vue.component('event_cards', EventCards)

var EventMap = require('./event_map.vue')
Vue.component('event_map', EventMap)

var home = new Vue({
    delimiters: ['[{', '}]'],
    el: 'main',
    data: {
        events: [],
        components: [
            EventControls,
            EventCards,
            EventMap,
        ]
    }
})