loc=window.location.toString();

$('nav a').each(function (){
    h=$(this).attr('data-href');
    if(loc.indexOf(h)!=-1){
        $(this).addClass('active');
    }
    else
    {
        $(this).removeClass('active');
    }
});



    if($(this).scrollTop() > 500) {
        $('#toTop').fadeIn(0);
    }else{
        $('#toTop').fadeOut(0);
    }
$(window).scroll(function() {
    if($(this).scrollTop() > 500) {
        $('#toTop').fadeIn(1000);
    }else{
        $('#toTop').fadeOut(1000);
    }
});
$('#toTop').click(function() {
    $('body,html').animate({scrollTop:0},800);
});

