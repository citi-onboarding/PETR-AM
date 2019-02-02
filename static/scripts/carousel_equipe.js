$(document).ready(function(){
    $('.carousel').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        dots: true,
        arrows: true,
        
        // define configurações quando for mobile
        responsive: [
            {
              breakpoint: 750,
              settings: {
                // centerMode: true,
                slidesToShow: 1,
                slidesToScroll: 1,
                infinite: true,
                dots: true,
                arrows: true,
              }
            }
        ]
    });
});