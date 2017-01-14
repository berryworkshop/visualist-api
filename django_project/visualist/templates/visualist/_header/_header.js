// Shorthand for $( document ).ready()
$(function() {
    var state = {
        browse_modal: false
    }

    // controls
    $('.browse_modal_toggle').on( "click", toggle_browse_modal)

    // esc key
    // hat tip http://stackoverflow.com/a/3369743/652626
    document.onkeydown = function(evt) {
        evt = evt || window.event
        var isEscape = false
        if ("key" in evt) {
            isEscape = (evt.key == "Escape" || evt.key == "Esc")
        } else {
            isEscape = (evt.keyCode == 27)
        }
        if (isEscape) {
            state.browse_modal = false
        }
        update_state()
    }

    function toggle_browse_modal() {
        var x = state.browse_modal
        state.browse_modal = (x == true ? false : true)
        update_state()
    }

    function update_state() {
        // browse modal
        if (state.browse_modal==true) {
            $('#browse_modal').removeClass('hide')
        } else {
            $('#browse_modal').addClass('hide')
        }
    }
})