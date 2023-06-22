$(document).ready(function(){
    $(window).scroll(function(){
        $("nav").toggleClass("scrolled", $(this).scrollTop() > 20);
    })
    });
    $(document).click(
      function (event) {
          var target = $(event.target);
          var _mobileMenuOpen = $(".navbar-collapse").hasClass("show");
          if (_mobileMenuOpen === true && !target.hasClass("navbar-toggler")) {
              $("button.navbar-toggler").click();
          }
      }
    );
    $(document).ready(function(){
      $("#see-more-bundles").hide();      
        $("#hide-and-show").click(function(){
      
          $("#see-more-bundles").toggle(1500);
      
        });
      
      });
    window.onscroll = function() {scrollFunction()};
    
    function scrollFunction() {
      if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("navbar").style.padding = "0 0 0 0";
      } else {
        document.getElementById("navbar").style.padding = "25px 0 10px 0";
      }
    }