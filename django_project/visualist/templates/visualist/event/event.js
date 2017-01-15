var Refs = require('../components/Refs.vue')
Vue.component('refs', Refs)


var SecondaryVisuals = Vue.component('secondary_visuals', {
    template: `
        <ul>
            <h3>Secondary Visuals</h3>
            <mini_tile></mini_tile>
            <mini_tile></mini_tile>
            <mini_tile></mini_tile>
        </ul>`
})

var MiniTile = Vue.component('mini_tile', {
    template: `
        <div>
            <img class="secondary_visual" />
            <p>This is a caption.</p>
        </div>`
})

var RelatedItems = Vue.component('related_items', {
    template: `
        <ul>
            <h3>Related Items</h3>
            <ul>
                <li>Related Item</li>
                <li>Related Item</li>
                <li>Related Item</li>
            </ul>
        </ul>
    `
})

var Controls = Vue.component('controls', {
    template: `
        <div>
            <h3>Controls</h3>
            <ul>
                <li>New</li>
                <li>Edit</li>
                <li>Delete</li>
                <li>Map it</li>
                <li>Featured</li>
                <li>Bookmark</li>
                <li>Add to Bucket List</li>
                <li>
                    <h4>Cite</h4>
                    <ul>
                        <li>APA</li>
                        <li>Chicago</li>
                        <li>MLA</li>
                    </ul>
                </li>
                <li>
                    <h4>Permissions</h4>
                    <ul>
                        <li>Public</li>
                        <li>Private</li>
                    </ul>
                </li>
                <li>
                    <h4>Share</h4>
                    <ul>
                        <li>Email</li>
                        <li>Facebook</li>
                        <li>Pinterest</li>
                    </ul>
                </li>
                <li>
                    <h4>Add to List</h4>
                    <ul>
                        <li>Checklist</li>
                        <li>Bookmarks</li>
                    </ul>
                </li>
            </ul>
        </div>`
})

var event = new Vue({
    delimiters: ['[{', '}]'],
    el: 'main',
    data: {
        obj: {
            title: '',
            date_start: 'January 1, 2014',
            date_end: false,
            description: `Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit.`,
        },
        components: [
            SecondaryVisuals,
            MiniTile,
            Refs,
            RelatedItems,
            Controls
        ]
    },
    mounted: function() {
        $.ajax({
            context: this,
            url: "/calendar/events/1.json",
        }).done(function(data) {
            this.obj.title = data.name      
        })
    }
})

