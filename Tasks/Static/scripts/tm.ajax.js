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
            alert(data);
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