$(document).ready(function() {
  console.log('ready');
    $("#main_button").click(function(evt) {
      evt.preventDefault();
      console.log("main button is clicked");
      var songName = $('#text_box')[0].value;
      var model =  document.getElementById("model_selection").value;
      const data = {chosen_model: model};
      // get request
      $.ajax({
        // put your api endpoint here
        url: 'https://project-billboard-api.herokuapp.com/predict/'+songName,
        type: "POST",
        data: JSON.stringify(data),
        dataType: "json",
        contentType: 'application/json',
        // function callback after success ajax request
        success: function(data) {
          console.log(data)

          document.getElementById("predict_result").style.backgroundColor = "rgb(100,100,100,0.8)"
          document.getElementById("predict_result").innerHTML = "The probability of "+songName+" being a hit song is: "+data["popularity"];
          $('#text_box')[0].value = "";
          // $('#text_box')[0].value = JSON.stringify(data)
        },
        error: function(error) {
          console.log('Error ${error}')
        },
      });

    }); 
    $('#nav_models').click(function(evt) {
        evt.preventDefault();
      $('html, body').animate({
        scrollTop: ($('#models').offset().top)
      },700);
    });
    $('#nav_about').click(function(evt) {
        evt.preventDefault();
      $('html, body').animate({
        scrollTop: ($('#about').offset().top)
      },700);
    });
    $('#nav_team').click(function(evt) {
        evt.preventDefault();
      $('html, body').animate({
        scrollTop: ($('#team').offset().top)
      },700);
    });
});