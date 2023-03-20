var headerAnimation = lottie.loadAnimation({
  container: document.querySelector('.left-image'), // the dom element that will contain the animation
  renderer: "svg",
  loop: false,
  autoplay: true,
  path: "/static/image/homeimage.json" // the path to the animation json
});
var darkmode = lottie.loadAnimation({
  container: document.querySelector('#darkbutton'), // the dom element that will contain the animation
  renderer: "svg",
  loop: false,
  autoplay: true,
  path: "/static/image/darkmode.json" // the path to the animation json
});

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    const square = entry.target.querySelector('.bottom-text-slider');

    if (entry.isIntersecting) {
      square.classList.add('bottom-text-slider-animation');
      headerAnimation.playSegments([0, 300], true);
      return; // if we added the class, exit the function
    }

    // We're not intersecting, so remove the class!
    square.classList.remove('bottom-text-slider-animation');
  });
});

const observer1 = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    const square = entry.target.querySelector('.bottom-text-slider');

    if (entry.isIntersecting) {
      square.classList.add('bottom-text-slider-animation');
      return; // if we added the class, exit the function
    }

    // We're not intersecting, so remove the class!
    square.classList.remove('bottom-text-slider-animation');
  });
});
observer.observe(document.querySelector('.right-content-home'));
observer1.observe(document.querySelector('.about-image'));


function startLoader() {
  
  window.addEventListener("DOMContentLoaded", function (event) {
    setTimeout(function () {
      if($.cookie('theme')=="dark"){
        changedarkbutton();
      }
      $('.loader').slideUp(700);
      $('.main-text-container').show();

      headerAnimation.playSegments([0, 300], true);
      

    }, 3500);

  });
}

// function startLoader() {

//   window.addEventListener("DOMContentLoaded", function(event) {
//     setTimeout(function() {
//       $('.loader').slideUp(100);
//       $('.main-text-container').show();

//       headerAnimation.playSegments([0, 300], true);

//     }, 100);

//   });
// }

startLoader();

var i = 0;
function changedarkbutton() {
  if (i == 0) {
    darkmode.playSegments([0, 10], true);
    i = 1;
    var x = document.querySelectorAll('.x path')
    x.forEach(elem => elem.setAttribute("stroke", "#ff6700"))
  }
  else {
    darkmode.playSegments([10, 0], true)
    i = 0;
    var x = document.querySelectorAll('.x path')
    x.forEach(elem => elem.setAttribute("stroke", "black"))
  }

}

