$(document).ready(function () {

    $("#btn_send").click(function () {
        /**
       * Function on click to button send.   
       */
        $("*").css("cursor", "progress"); /* set cursor in progress during the process */

        var comment = $("#comment").val().toString();

        if (comment != "") {

            $(".row#card_history_rec").append('<div class="col-10"><div class="card bg-light mb-3 mw-100"><div class="card-header">Me</div><div class="card-body"><p class="card-text">' + comment + '</p></div></div></div>');/* add card light , for user */

            $("#comment").val("Que peut tu me dire sur : ") /* set value default to aretext , This is an example for user */

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
                    console.log(response);

                    if ('lat' in response) {
                        $(".row#card_history_rec").append('<div class="col-10"><div class="card text-white bg-dark mb-3 mw-100"><div class="card-header">Grand Py</div><div class="card-body"><p class="card-text">' + response.text + response.name + '</p></div></div></div>');/* add card dark , for grandpy with the response.text + response.name */

                        initMap(response.lat, response.lng, response.name)

                        Hitory(response.wiki_text);
                    }
                    else {
                        $(".row#card_history_rec").append('<div class="col-10"><div class="card text-white bg-dark mb-3 mw-100"><div class="card-header">Grand Py</div><div class="card-body"><p class="card-text">' + response.text + '</p></div></div></div>');
                        /* add card dark , for grandpy with the respense.text*/

                    }

                    $(".card-history").scrollTop($(".card-history")[0].scrollHeight); /* go down to the bottom of the div */

                    $("*").css("cursor", "default"); /* set cursor in default in the last of the process */

                    $("#comment").val("Que peut tu me dire sur : ")
                },
                error: function (error) {

                    $("*").css("cursor", "default"); /* set cursor in default in the last of the process */

                    console.log(error);
                }
            });

        }
    });

    $('#comment').keypress(function (e) {
        /* function for press enter in #comment areatext execute a function click */
        if (e.which == 13) {
            $('#btn_send').click();

        }
    });


    let map;

    function initMap(lati, longi, description_) {
        /**
       * initialyse the maps google in the div #map-canvas
       * @param  {float} lati latitude of location.
       * @param  {float} longi longitude of location.
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

    function Hitory(text_hist) {
        /**
       * Get the history text on wiki_text for json return
       * @param  {float} text_hist text .
       * @return {google.maps.Map}      A object to return and display to div.
       */
        text_hist = "Une petite histoire ne fait pas de mal. ! :D   >   " + text_hist /* set a default text to user */
        $(".row#card_history_rec").append('<div class="col-10"><div class="card text-white bg-dark mb-3 mw-100"><div class="card-header">Grand Py</div><div class="card-body"><p class="card-text">' + text_hist + '</p></div></div></div>'); /* add card dark , it's grand py card*/
    }

});





