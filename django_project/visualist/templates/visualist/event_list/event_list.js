var Events = require('../../../components/Events.vue')
Vue.component('events', Events)

var home = new Vue({
    delimiters: ['[{', '}]'],
    el: 'main',
    data: {
        events: [],
        components: [
            Events
        ]
    }
})

