jQuery("document").ready(function($){
    
    /*var nav = $('.nav-total');*/
    var principal = $('.principal-menu');
    var navbar = $('.nav-total-a');
    var interna = $('.containerinterna-fixo');
    var programaFixo = $('.programa-fixo');
    var nav2 = $('.nav-buscar2');
    var sidebar = $('.sidebar-fixa');

    $(window).scroll(function () {
        if ($(this).scrollTop() > 120) {
            /*
            nav.addClass("f-nav");*/
            principal.addClass("separa");
            navbar.addClass("nav-total-show");
            nav2.addClass("nav-buscar");


        } else {
            /*
            nav.removeClass("f-nav");*/
            principal.removeClass("separa");
            navbar.removeClass("nav-total-show");
            nav2.removeClass("nav-buscar");

        }

        if ($(this).scrollTop() > 330) {
            programaFixo.addClass("fixar-programa");
            /*interna.addClass("containerinterna-fixo-a");*/
        } else {
            programaFixo.removeClass("fixar-programa");
            /*interna.removeClass("containerinterna-fixo-a");*/
        }

        if ($(this).scrollTop() > 1119) {
            sidebar.addClass("sidebar-mostrar");
            /*interna.addClass("containerinterna-fixo-a");*/
        } else {
            if ($(this).scrollTop() > 1119) {
                sidebar.addClass("sidebar-mostrar");
                /*interna.addClass("containerinterna-fixo-a");*/
            }
            sidebar.removeClass("sidebar-mostrar");
            /*interna.removeClass("containerinterna-fixo-a");*/
        }
        /*
        if ($(this).scrollTop() > 610) {

            interna.removeClass("containerinterna-fixo-a");

        }*/
    });
 
});