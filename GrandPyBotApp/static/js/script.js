$(document).ready(function(){

    $("#btn_send").click(function(){
        var comment = $("#comment").val().toString();
        if ( comment != "")
        {                        
            
            $(".row").append('<div class="col-10"><div class="card bg-light mb-3 mw-100"><div class="card-header">Me</div><div class="card-body"><p class="card-text">'+  comment + '</p></div></div></div>');

            $("#comment").val('')

            $(".card-history").scrollTop($(".row").height()); 

        }

    });
    
});




