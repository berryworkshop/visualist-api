var EventCards = require('./event_cards.vue')
Vue.component('event-cards', EventCards)

var EventMap = require('./event_map.vue')
Vue.component('event-map', EventMap)

window.vue = new Vue({
    delimiters: ['[{', '}]'],
    el: 'main',
    data: {
        panel: 'list',
        panels_collapsed: true,
        components: [
            EventCards,
            EventMap,
        ]
    },
    methods: {
        panelHidden: function(panel) {
            // determine if a panel should be hidden or not
            var hide = (this.panels_collapsed && panel != this.panel) ? true : false;
            return hide;
        },
        showPanel: function(panel) {
            // show a panel
            this.panel = panel
            Vue.nextTick(function() {
                // resizes map to fit width, difficult/impossible when off screen
                this.$refs.map_component.$data.map.invalidateSize()
            }.bind(this))
        }
    }
})