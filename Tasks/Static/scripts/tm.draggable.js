/**
 * Created by PyCharm.
 * User: Alex
 * Date: 06.02.12
 * Time: 9:37
 * To change this template use File | Settings | File Templates.
 */
$(function() {
$( "#draggable" ).draggable({
    //delay: 1000
    //distance: 20
    //snap: true
    revert: true,
    helper: "clone",
    handle: "h3"
});
});