var pakege={};
var mass=[];
var objAjax={
                type:'POST',
                timeout:50000,
                error: function(){alert('ошибка');
                                loader.fadeOut(300);
                                },
                success: function(data){
                        $('#content2').html(data);
                        loader.fadeOut(300);
                },
                url:'/inspection/',
            };

var loader=$('#preloader');
loader.fadeOut(sel);


for(var i =0;i<200;i++){
    mass[i]=i;
}
$('#content2 > ul > li > ul >li').click(
    function(){
        s=$(this)
        p=$(this).parents('li');
        if(s.hasClass('chk')){

            p.removeClass('actLi');
            s.removeClass('chk');
            delete pakege[p.attr('data-id')];

        }else
        {
            $('li',p).removeClass('chk');
            s.addClass('chk');
            p.addClass('actLi');
            pakege[p.attr('data-id')]=s.children('span').html();

        }


});
$('.bt').click(function(){

        objAjax.data='jsonData=' + JSON.stringify(pakege);
        $.ajax(objAjax);
        loader.fadeIn(300);


});



$('#content2 select').change(sel);

function sel(){
    $("#content2>ul>li").fadeIn(300);
    //alert(parseInt(200-$(this).val()));
    var a;
    massL=mass.slice();
    massL2=mass.slice();
    for (var i=0;i<200-parseInt($(this).val());i++){
         b=randM(massL);
        $("#content2>ul>li").slice(b,b+1).fadeOut(300);
    }
}
function randM(m){
    while(true){
       a=Math.floor(Math.random()*199);
        if(m[a]!=null){
           v=m[a];
           m[a]=null;
           return v;
        }
    }
}
$('header li').addClass('testsL');

 function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
