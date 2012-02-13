/**
 * Created by PyCharm.
 * User: aandruschenko
 * Date: 02.02.12
 * Time: 13:43
 * To change this template use File | Settings | File Templates.
 */
/** Accordion control jquery script*/
$(function() {
    var stop = false;
    $( "#accordion h3" ).click(function( event ) {
        if ( stop ) {
            event.stopImmediatePropagation();
            event.preventDefault();
            stop = false;
        }
    });
    $( "#accordion" )
        .accordion({
            header: "> div > h3",
            collapsible: true,
            autoHeight: true
        })
        .sortable({
            placeholder: "ui-state-highlight",
            axis: "y",
            handle: "h3",
            stop: function() {
                stop = true;
            }
        })
});

