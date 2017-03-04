loc=window.location.toString();

$('nav a').each(function (){
    h=$(this).attr('href');
    h=h.slice(h.lastIndexOf('/')+1);
    if(loc.indexOf(h)!=-1){
        $(this).addClass('active');
    }
    else
    {
        $(this).removeClass('active');
    }
});
