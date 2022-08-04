


$(document).ready(function () {
  $(document).bind('keydown', function(e) {
    if(e.ctrlKey && (e.which == 83)) {
      e.preventDefault();
      return false;
    }
  });
  $('#menu').click(function () {
    $('#menu').toggleClass('rotate');
    $('.navbar-main').toggleClass('nav-transform');
    //$('.nav-page2').classList.toggle('transform')
    $('.menu-line1').toggleClass('rotate1');
    $('.menu-line2').toggleClass('rotate2');
  });

  $('.navlink').click(function () {
    $('#menu').toggleClass('rotate')
    $('.navbar-main').toggleClass('nav-transform')
    //$('.nav-page2').classList.toggle('transform')
    $('.menu-line1').toggleClass('rotate1')
    $('.menu-line2').toggleClass('rotate2')
  });

});

$(document).ready(function () {

  $("#prjslider").owlCarousel({
    nav: true,
    items: 1,
    loop: true,
    animateIn: 'animate__jackInTheBox',
    smartSpeed:450,
    navText: ['<img src="https://img.icons8.com/sf-regular/48/000000/left.png"/>', '<img src="https://img.icons8.com/sf-regular/48/000000/right.png"/>']
  });

  // var owl = $('#prjslider');
  // owl.owlCarousel();
  // // Go to the next item
  // $('#prjslider .owl-nav button.owl-next').click(function () {
  //   $('.project-image-outer').addClass("prj-anim");
  //   owl.trigger('next.owl.carousel',[2000]);
  // })
  // // Go to the previous item
  // $('.customPrevBtn').click(function () {
  //   // With optional speed parameter
  //   // Parameters has to be in square bracket '[]'
  //   owl.trigger('prev.owl.carousel', [300]);
  // })

});

$(document).ready(function () {
  var fadetime = 3000;
  var delaytime = 1400;
  function carousel() {
    $('.entry:first-child').fadeIn(3000).queue(function () {
      $(this).fadeOut(500).appendTo('.entries').dequeue();
    });

  }
  carousel();
  setInterval(function () { carousel() }, 3500);
});

$(document).on('click', 'a[href^="#"]', function (event) {
  event.preventDefault();
  console.log("As")
  $('html, body').animate({
      scrollTop: $($.attr(this, 'href')).offset().top
  }, 1000);
});