$(document).ready(function () {
checkTheme();
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


$(document).ready(function () {

  $("#prjslider").owlCarousel({
    nav: true,
    items: 1,
    loop: true,
    animateIn: 'animate__jackInTheBox',
    smartSpeed: 450,
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



// DARKMODE
if (typeof $.cookie('theme') === 'undefined'){
  $.cookie('theme',"white")
}


function checkTheme() {
  var theme = $.cookie('theme')
  if (theme == "dark") {
    document.documentElement.style.setProperty('--colorTextBody', '#ffffffdb');
    document.documentElement.style.setProperty('--black', '#fff');
    $('body').addClass('darkmode');
    $('.dev-text').addClass('dev-text-darkmode');
    $('.dev-textd').addClass('dev-textd-darkmode');
    $('.my-journey-outer').addClass('my-journey-outer-dark');
    $('.my-journey-card-content').addClass('my-journey-card-content-dark');
    $('.my-journey-card').addClass('my-journey-card-dark');
    $('.skill-item').addClass('skill-item-dark');
    $('.navbar-main').addClass('navbar-main-dark');

  }else{
    document.documentElement.style.setProperty('--colorTextBody', 'rgb(var(--rgbText) / 0.8');
    document.documentElement.style.setProperty('--black', '#000');
    $('body').removeClass('darkmode');
    $('.dev-text').removeClass('dev-text-darkmode');
    $('.dev-textd').removeClass('dev-textd-darkmode');
    $('.my-journey-outer').removeClass('my-journey-outer-dark');
    $('.my-journey-card-content').removeClass('my-journey-card-content-dark');
    $('.my-journey-card').removeClass('my-journey-card-dark');
    $('.skill-item').removeClass('skill-item-dark');
    $('.navbar-main').removeClass('navbar-main-dark');

  }

}

$('#darkbutton').click(function () {
  if($.cookie('theme')=="dark"){
    $.cookie('theme',"white")
  }else{
    $.cookie('theme',"dark")
  }
  checkTheme()
  // $('body').toggleClass('darkmode');
  // $('.dev-text').toggleClass('dev-text-darkmode');
  // $('.dev-textd').toggleClass('dev-textd-darkmode');
  // $('.my-journey-outer').toggleClass('my-journey-outer-dark');
  // $('.my-journey-card-content').toggleClass('my-journey-card-content-dark');
  // $('.my-journey-card').toggleClass('my-journey-card-dark');
  // $('.skill-item').toggleClass('skill-item-dark');

});     