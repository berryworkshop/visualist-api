<template>
    <div class="panel">
        <button type="button"><i class="fa fa-sort" aria-hidden="true"></i> Sort</button>
        <ul class="card_list">
            <li v-for="obj in object_list" class="card">
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
        name: 'event_cards',
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
    @import "../_grid.scss";
    @import "../_utility.scss";

    .card_list {
        display: flex;
        flex-wrap: wrap;
    }
</style>