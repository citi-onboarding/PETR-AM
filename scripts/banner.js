$(document).ready(function(){
    $('#bannerGroup').slick({
        nextArrow: '<button type="button" id="bannerNext"><div id="bannerSetaR"></div></button>',
        prevArrow: '<button type="button" id="bannerPrev"><div id="bannerSetaL"></div></button>',
        infinite: true,
        autoplay: true,
        autoplaySpeed: 3000
});
});