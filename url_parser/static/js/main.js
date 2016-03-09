$(document).ready(function() {

    var intervalID;

    function startParsing() {
        $.ajax({
            type: "GET",
            url: "/ajax/parse/",
            success: function(data){
                intervalID = setInterval(refresh(), 1000);
            },
            error: function() {

            }
        });
    }

    function refresh() {
        $.ajax({
            type: "GET",
            url: "/ajax/refresh/",
            success: function(data){
                for (i = 0; i < data.length; i++) {
                    $('#left_'+data[i].id).replaceWith('<li><b><Дата '+data[i].time+'></b>: '+data[i].url+', '+(data[i].success ? '<b style="color:green">success</b>':'<b style="color:red">error</b>')+'</li>');
                    if (data[i].title || data[i].h1 || data[i].charset) {
                        $('#right_' + data[i].id).replaceWith('<li><b>' + data[i].url + '</b> - ' + data[i].title + ', ' + data[i].h1 + ', ' + data[i].charset + '</li>');
                    }
                }
            },
            error: function() {
                clearInterval(intervalID);
            }
        });
    }

    $('.parse').click(function(){
        startParsing();
    });

});