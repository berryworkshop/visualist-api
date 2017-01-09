// Shorthand for $( document ).ready()
$(function() {
    var state = {
        browse_modal: false
    }

    $('.browse_modal_toggle').on( "click", toggle_browse_modal)

    function toggle_browse_modal() {
        var x = state.browse_modal
        state.browse_modal = (x == true ? false : true)
        update_state()
    }

    function update_state() {
        $('#browse_modal').toggleClass('visually_hidden')
    }
})