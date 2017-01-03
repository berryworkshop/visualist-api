require('./controls.tag')
require('./secondary_visuals.tag')
require('./related_items.tag')
require('./source.tag')
require('./cross_refs.tag')

<main>
    <h1>Title</h1>
    <p>Other titles</p>

    <h2>Friday, January 6, 2017</h2>
    <h2>Chicago Artist Coalition</h2>
    <p>1234 Anywhere St.</p>
    <p>Chicago, IL 60600</p>

    <p>Distance to this event from your current location: 123 miles</p>

    <img class="primary_visual" />
    <p>This is a caption for the above visual.</p>

    <h3>Description</h3>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    <p>Other Descriptions</p>

    <secondary_visuals></secondary_visuals>

    <p>Record created by admin on January 1, 2017</p>
    <source></source>

    <cross_refs></cross_refs>

    <related_items title="Related Items"></related_items>
    <related_items title="Similar Items"></related_items>

    <controls></controls>

    <style>
        main {
            background-color: #eee;
        }
        .primary_visual {
            width: 300px;
            height: 300px;
            background-color: #ddd;
        }
    </style>
</main>