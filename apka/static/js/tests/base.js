mass=[]
for(var i =0;i<200;i++){
    mass[i]=i;
}

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

sel();

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