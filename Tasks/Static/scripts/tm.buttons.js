/**
 * Created by PyCharm.
 * User: Alex
 * Date: 13.02.12
 * Time: 9:37
 * To change this template use File | Settings | File Templates.
 */
/** Buttons on main page */

(function() {
    $(document).ready(function() {
        $( ".sort_button" ).button({
            text: false,
            icons: {
                primary: "ui-icon-carat-2-n-s"
            }
        });
        $( ".drag_button" ).button({
            text: false,
            icons: {
                primary: "ui-icon-clock"
            }
        });
    })
})();