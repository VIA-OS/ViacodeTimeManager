/**
 * Created by PyCharm.
 * User: aandruschenko
 * Date: 16.02.12
 * Time: 12:58
 * To change this template use File | Settings | File Templates.
 */
(function() {
    $(document).ready(function() {
        $.get("/list_tasks_ajax"
            , function(data) {
            /**alert(data);**/
            html = new EJS({url: urlContainer.static + 'templates/tm.tasks.ejs'}).render(data)
            $('#accordion').html(html);
        });
    });
    /**$.post("/list_tasks_ajax", {
            name: "Berg",
            food: "Code"
        },
        function(data) {
            alert(data);
        }
    );*/
})();