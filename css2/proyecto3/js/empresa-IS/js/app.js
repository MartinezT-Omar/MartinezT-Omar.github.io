$('#slider').owlCarousel({/*llamado a la funcion owlcarousel*/
    loop:true, /*realiza un ciclo*/
    autoplay:true, /*ciclo automatico*/
    responsive:{ /*slide adaptativo a las pantallas*/
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:1
        }
    }

})