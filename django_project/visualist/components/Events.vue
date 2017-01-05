<template>
    <div>
        <span class="button_group">
            <a class="button" href="#"><i class="fa fa-sort" aria-hidden="true"></i> Sort</a>
            <a class="button" href="#">Filter</a>
        </span>
        <ul class="event_list">
            <li v-for="obj in object_list" class="event">
                <img class="event_image" />
                <div class="event_info">
                    <h3 class="md event_title"><a :href="obj.get_absolute_url">{{ obj.name }}</a></h3>
                    <p class="md event_when_where"><strong>Chicago Artist Coalition</strong>: Jan 1 - Jan 7, 2017</p>
                    <p class="md event_synopsis">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor.</p>
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
            border: 1px solid #ccc;
            border-bottom: 0;
            padding: .5rem;
            list-style-type: none;
            display: flex;
            
            .event_image {
                min-width: 4rem; 
                height: 4rem;
                background-color: #ddd;              
            }

            .event_info {
                flex: auto;
                padding: 0 .5rem;
                flex-wrap: wrap;

                .event_title {
                    margin: 0 0 .5em 0;
                    a {
                        text-decoration: none;                    
                    }
                }

                .event_when_where,
                .event_synopsis {
                    margin: 0 0 .5em 0;
                    font-size: smaller;
                }

                .event_when_where {}
                .event_synopsis {
                    color: #777;
                }
            }
            .event_controls {
                margin-top: .5rem;    
                white-space: nowrap;

                .button {}
            }
        }

        .event:last-child {
            border-bottom: 1px solid #ccc;
        }
    }
</style>