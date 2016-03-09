$(document).ready(function() {

    /**
     *  This function initialize parsing process in the server side
     */
    function startParsing() {
        $.ajax({
            type: "GET",
            url: "/ajax/start/",
            success: function(data){
                refresh();
            },
            error: function(error) {
                parsingDone();
            }
        });
    }

    /**
     *  This function request some new info from the server that collecting while parsing
     */
    function refresh() {
        $.ajax({
            type: "GET",
            url: "/ajax/refresh/",
            success: function(data){
                console.log('refresh success');

                if (Array.isArray(data)) {
                    for (i = 0; i < data.length; i++) {
                        $('#left_' + data[i].id).replaceWith('<li><b><Дата ' + data[i].time + '></b>: ' + data[i].url + ', ' + (data[i].success ? '<b style="color:green">success</b>' : '<b style="color:red">error</b>') + '</li>');
                        if (data[i].title || data[i].h1 || data[i].charset) {
                            $('#right_' + data[i].id).replaceWith('<li><b>' + data[i].url + '</b> - ' + data[i].title + ', ' + data[i].h1 + ', ' + data[i].charset + '</li>');
                        }
                    }
                }

                setInterval(refresh(), 1000);
            },
            error: function(error) {
                parsingDone();
            }
        });
    }

    /**
     *  writes 'parsing is done' when it's done
     */
    function parsingDone() {
        $('.parse').after('<b style="color:green; margin-left:20px" >Parsing is done.</b>')
    }

    /**
     *  if button pressed, then we start parse URLs
     */
    $('.parse').click(function(){
        startParsing();
    });

});