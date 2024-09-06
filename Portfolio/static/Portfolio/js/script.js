// Toggle the .scrolled class on header when the page is scrolled
window.addEventListener("scroll", function () {
  var header = document.getElementById("header");
  if (window.scrollY > 50) {
    header.classList.add("scrolled");
  } else {
    header.classList.remove("scrolled");
  }
});

//document.querySelector('.hamburger').addEventListener('click', function() {
//document.querySelector('.navbar ul').classList.toggle('show');});


// Toggle the .show class on menu and manage the padding of .presentation
document.querySelector('.hamburger').addEventListener('click', function() {
  var menu = document.querySelector('.navbar ul');
  var body = document.body;
  
  menu.classList.toggle('show');
  
  if (menu.classList.contains('show')) {
      body.classList.add('header-menu-open');
  } else {
      body.classList.remove('header-menu-open');
  }
});















/*


document.querySelector(".hamburger").addEventListener("click", function () {
  var menu = document.querySelector(".navbar ul");
  var body = document.body;

  menu.classList.toggle("show");

  if (menu.classList.contains("show")) {
    body.classList.add("header-menu-open");
  } else {
    body.classList.remove("header-menu-open");
  }
});*/