$('header li').bind('click',function(){
    if(!$(this).hasClass('testsL')){
    $('header li.active').removeClass('active');
    $(this).addClass('active');
    objAjax.url='/editLan/';
    objAjax.data=  {'globLang': $('header li.active').attr('data-index')};
    $.ajax(objAjax);
    }
});


var objAjax={
                type:'POST',
                timeout:50000,
                error: function(){alert('ошибка')},
                success: function(){window.location.reload();},

            };

$('#imSub').click(function(){
    $('#logout form').submit();

});

$('.cent').parents('section,#wrap').css('margin-top','31vh');
/*csrf_token */

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
