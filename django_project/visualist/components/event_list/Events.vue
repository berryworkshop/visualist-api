<template>
    <ul>
        <li v-for="obj in object_list">
            <a :href="obj.get_absolute_url">{{ obj.name }}</a>
        </li>
    </ul>
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