	
  // $(window).on('load', function () {
	// 	setTimeout(removeLoader,3200);
  // 	}); 
	//   function removeLoader(){
  //   $('.container').show()
	// 	$('.loader').slideUp(1000);
	// }
	$(document).ready(function(){
  $('#menu').click(function(){          
    $('#menu').toggleClass('rotate');
    $('.navbar-main').toggleClass('nav-transform');
      //$('.nav-page2').classList.toggle('transform')
    $('.menu-line1').toggleClass('rotate1');
    $('.menu-line2').toggleClass('rotate2');
  });

  $('.navlink').click(function(){
    $('#menu').toggleClass('rotate')
    $('.navbar-main').toggleClass('nav-transform')
      //$('.nav-page2').classList.toggle('transform')
    $('.menu-line1').toggleClass('rotate1')
    $('.menu-line2').toggleClass('rotate2')
  });
    
});

$(document).ready(function(){
  var fadetime = 3000;
  var delaytime = 1400;
  function carousel(){
    $('.entry:first-child').fadeIn(3000).queue(function(){
      $(this).fadeOut(500).appendTo('.entries').dequeue();
    });
    
  }
  carousel();
  setInterval( function(){ carousel() }, 3500);
});
  
