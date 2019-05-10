$(document).ready(function() {
  console.log('ready');

  // Collapse Navbar
  var navbarCollapse = function() {
    if ($("#mainNav").offset().top > 400) {
      $("#mainNav").addClass("navbar-shrink");
    } else {
      $("#mainNav").removeClass("navbar-shrink");
    }
  };
  // Collapse now if page is not at top
  navbarCollapse();
  // Collapse the navbar when page is scrolled
  $(window).scroll(navbarCollapse);

  // Handle click events
  $("#main_button").click(function(evt) {
    evt.preventDefault();
    console.log("main button is clicked");
    var songName = $('#text_box')[0].value;
    var model =  document.getElementById("model_selection").value;
    const data = {chosen_model: model};

    if (songName !== "") {
      // get request
      var $this = $(this);
      var loadingText = '<i class="fa fa-spinner fa-spin"></i> Predicting...';
      if ($(this).html() !== loadingText) {
        $this.data('Predict', $(this).html());
        $this.html(loadingText);
      }
      $.ajax({
        // put your api endpoint here
        url: './api/v1/predict/'+songName,
        type: "POST",
        data: JSON.stringify(data),
        dataType: "json",
        contentType: 'application/json',
        // function callback after success ajax request
        success: function(data) {
          console.log(data)
          $this.html($this.data('Predict'));
          $('#text_box')[0].value = "";
          if (data["popularity"] == "NAN") {
          	document.getElementById("predict_result").style.backgroundColor = "rgb(100,100,100,0.8)"
      		  document.getElementById("predict_result").innerHTML = "Sorry, your requested song cannot be found.";
          } else {
            document.getElementById("predict_result").style.backgroundColor = "rgb(100,100,100,0.8)";
            document.getElementById("predict_result").innerHTML = "The probability of "+songName+" being a hit song is: "+data["popularity"];
      	  }
        },
        error: function(error) {
          console.log('Error ${error}')
        },
      });
    } else {
      document.getElementById("predict_result").style.backgroundColor = "rgb(100,100,100,0.8)"
      document.getElementById("predict_result").innerHTML = "Please key in a song name!";
    }
  }); 
  document.getElementById('text_box').addEventListener('keypress', function(event) {
    if (event.keyCode == 13) {
      event.preventDefault();
      document.getElementById("main_button").click();
    }
  });
  $('#nav_home').click(function(evt) {
      evt.preventDefault();
    $('html, body').animate({
      scrollTop: 0
    },700);
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
  $('#nav_timeline').click(function(evt) {
      evt.preventDefault();
    $('html, body').animate({
      scrollTop: ($('#timeline').offset().top)
    },700);
  });
  $('#nav_team').click(function(evt) {
      evt.preventDefault();
    $('html, body').animate({
      scrollTop: ($('#team').offset().top)
    },700);
  });
});