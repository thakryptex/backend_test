$(document).ready(function() {

    $('.parse').click(function(){

        $.ajax({
            type: "GET",
            url: "/ajax/parse/",
            success: function(data){
                for (i = 0; i < data.length; i++) {
                    $('#left_'+data[i].id).replaceWith('<li><Дата '+data[i].time+'>: '+data[i].url+', '+(data[i].success ? 'success':'error')+'</li>');
                    $('#right_'+data[i].id).replaceWith('<li>'+data[i].url+' - '+data[i].title+', '+data[i].h1+', '+data[i].charset+'</li>');
                }
            }
        });

    });

});