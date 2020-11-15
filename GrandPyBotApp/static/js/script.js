$(document).ready(function () {

    $("#btn_send").click(function () {
        /**
       * Function on click to button send.   
       */
        $("*").css("cursor", "progress"); /* set cursor in progress during the process */

        var comment = $("#comment").val().toString();

        if (comment != "") {

            $(".row#card_history_rec").append('<div class="col-10"><div class="card bg-light mb-3 mw-100"><div class="card-header">Me</div><div class="card-body"><p class="card-text">' + comment + '</p></div></div></div>');/* add card light , for user */
            
            $('#comment').attr("placeholder", "Que peut tu me dire sur : "); 
           
             $('#comment').val("");
            /* set placeholder default to aretext , This is an example for user
            
            $(".card-history").scrollTop($(".card-history")[0].scrollHeight); /* go down to the bottom of the div */

            /*console.log(comment);*/

            $.ajax({
                /*ajax it's a function with send a http request to the server in the url @url*/
                type: 'POST',
                url: "/chat",
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                data: JSON.stringify({ data: comment }),

                success: function (response) {
                    //console.log(response);

                    if ('lat' in response) {
                        $(".row#card_history_rec").append('<div class="col-10"><div class="card text-white bg-dark mb-3 mw-100"><div class="card-header">Grand Py</div><div class="card-body"><p class="card-text">' + response.text + response.name + '</p></div></div></div>');/* add card dark , for grandpy with the response.text + response.name */

                        initMap(response.lat, response.lng, response.name)

                        Hitory(response.wiki_text, response.pageid);
                    }
                    else {
                        $(".row#card_history_rec").append('<div class="col-10"><div class="card text-white bg-dark mb-3 mw-100"><div class="card-header">Grand Py</div><div class="card-body"><p class="card-text">' + response.text + '</p></div></div></div>');
                        /* add card dark , for grandpy with the respense.text*/

                    }

                    $(".card-history").scrollTop($(".card-history")[0].scrollHeight); /* go down to the bottom of the div */

                    $("*").css("cursor", "default"); /* set cursor in default in the last of the process */

                   
                },
                error: function (error) {

                    $("*").css("cursor", "default"); /* set cursor in default in the last of the process */
                   
                    //console.log(error);
                }
            });

        }
    });

    $('#comment').keypress(function (e) {
        /* function for press enter in #comment areatext execute a function click */
        if (e.which == 13) {
            $('#btn_send').click();
            $(this).val('').focus();    
            return false;
            
        }
    });


    let map;

    function initMap(lati, longi, description_) {
        /**
       * initialyse the maps google in the div #map-canvas
       * Add marker red in the location lat and lng on the map
       * @param  {float} lati latitude of location.
       * @param  {float} longi longitude of location.
       * @param  {string} description_ description of location (title ex: Troyes, France).
       * @return {google.maps.Map}      A object to return and display to div.
       */
        map = new google.maps.Map(document.getElementById("map-canvas"), {
            center: { lat: lati, lng: longi },
            zoom: 13,/* zoom in google maps  */

        
        });

        new google.maps.Marker({
            position: { lat: lati, lng: longi },
            map,
            title: description_,
          });
    }

    initMap(45, 18, ""); /* initialise the google maps in the document ready in position lat = 45 and lng = 18 */

    function Hitory(text_hist, pageid) {
        /**
       * Get the history text on wiki_text for json return
       * @param  {string} text_hist text summary of wikipedia
       * @param  {interger} pageid pageid of wikipedia
       *
       */
        
        smiley_icon = '<svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-emoji-laughing" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M12.331 9.5a1 1 0 0 1 0 1A4.998 4.998 0 0 1 8 13a4.998 4.998 0 0 1-4.33-2.5A1 1 0 0 1 4.535 9h6.93a1 1 0 0 1 .866.5z"/> <path d="M7 6.5c0 .828-.448 0-1 0s-1 .828-1 0S5.448 5 6 5s1 .672 1 1.5zm4 0c0 .828-.448 0-1 0s-1 .828-1 0S9.448 5 10 5s1 .672 1 1.5z"/></svg>'
        text_tempo = "Une petite histoire ne fait pas de mal. ! " + smiley_icon
        text_hist =  " > " + text_hist + " <a href='https://fr.wikipedia.org/?curid=" + pageid + "' target='_blank' > En savoir plus sur Wikipédia </a> " /* set a default text to user */
        $(".row#card_history_rec").append('<div class="col-10"><div class="card text-white bg-dark mb-3 mw-100"><div class="card-header">Grand Py</div><h6 class="card-title">'+ text_tempo +'</h6><div class="card-body"><p class="card-text">' + text_hist + '</p></div></div></div>'); /* add card dark , it's grand py card*/
    }


});





