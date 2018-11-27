$(document).ready(function(){
    $('#servicosGroup').slick({
        nextArrow: '<button type="button" id="servicosNext"><img id="servicosSetaR" src="imagens/servicos/sNext.svg"></button>',
        prevArrow: '<button type="button" id="servicosPrev"><img id="servicosSetaL" src="imagens/servicos/sPrev.svg"></button>',
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        centerMode: true,
        draggable: false,
        responsive: [
            {
                breakpoint: 751,
                settings:{
                    slidesToShow: 1,
                    nextArrow: '<button type="button" id="servicosNext"><img id="servicosSetaR" src="imagens/servicos/sNext.svg"></button>',
                    prevArrow: '<button type="button" id="servicosPrev"><img id="servicosSetaL" src="imagens/servicos/sPrev.svg"></button>',
                    infinite: true,
                    slidesToScroll: 1,
                    centerMode: true,
                    draggable: false,
                    centerPadding: '20px'
                }
            }
        ]
});
});