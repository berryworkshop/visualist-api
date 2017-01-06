<template>
    <div>
        <span class="button_group">
            <a class="button" href="#"><i class="fa fa-sort" aria-hidden="true"></i> Sort</a>
            <a class="button" href="#">Filter</a>
        </span>
        <ul class="event_list">
            <li v-for="obj in object_list" class="event">
                <div class="event_visuals">
                    <img class="event_image" />
                    <h4 class="event_date_icon">Jan 1 – Jan 30</h4>
                    <p>More Images</p>
                </div>
                <div class="event_info">
                    <p class="location">Chicago: Pilsen @ Storefront Gallery</p>
                    <h3 class="title"><a <a :href="obj.get_absolute_url">{{ obj.name }}</a></h3>
                    <p class="synopsis">This is the synopsis.  It's limited to 255 characters.  Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisiut.</p>
                    <p class="audience">All ages welcome</p><!-- tiered as a vocab -->
                    <i class="fa fa-usd" aria-hidden="true"></i>    
                </div>
                <div class="event_controls">
                    <a class="button" href="#"><i class="fa fa-star" aria-hidden="true"></i></a>
                    <a class="button" href="#"><i class="fa fa-flag" aria-hidden="true"></i></a>
                </div>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: 'events',
        data() {
            return {
                object_list: [],
            }
        },
        mounted: function() {
            $.ajax({
                context: this,
                url: "/timeline/events.json",
            }).done(function(data) {
                this.object_list = data.results
            })
        }
    }
</script>

<style lang="sass" scoped>
    .button {
        padding: .5em;
        background-color: hsla(0,0%,0%,0.125);
        text-decoration: none;
    }

    .event_list {
        padding-left: 0;

        .event {
            background-color: white;
            margin-bottom: 1rem;
            list-style-type: none;
            display: flex;
            flex-direction: column;

            .event_visuals {
                flex: auto;
                height: 10rem;
                background-color: silver;
            }
            .event_info {
                padding: 1rem;

                .location {
                    font-size: smaller;
                }
                .title {
                    a {
                        text-decoration: none;
                    }
                }
                .synopsis {
                    font-style: italic;
                }
                .audience {}
            }
            .event_controls {
                padding: 1rem;
                padding-bottom: 1.5rem;
            }
        }

        .event:last-child {
            margin-bottom: none;
        }
    }
</style>