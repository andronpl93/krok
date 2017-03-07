mass=[]
for(var i =0;i<200;i++){
    mass[i]=i;
}
var coun=$('#content2 select').val();
$('#content2 > ul > li > ul >li').click(
    function(){
        if($(this).hasClass('tr'))
            $(this).css('background-color','rgba(0,128,0,0.5)');
        else
            $(this).css('background-color','rgba(255,0,0,0.5)');


    }
);
sel();
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
       a=Math.floor(Math.random()*(coun-1));
        if(m[a]!=null){
           v=m[a];
           m[a]=null;
           return v;
        }
    }
}

$('header li').addClass('testsL');