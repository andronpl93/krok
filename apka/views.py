from django.shortcuts import render
from django.http import HttpResponse
import urllib.request as ul
from .models import Lang,Classes,Booklets,Booklet
from bs4 import BeautifulSoup
import logging

globLang='ukr'

def start(request):
    code= Lang.objects.get(code=globLang)
    krok=Classes.objects.filter(lang=code)
    lang=Lang.objects.all()
    return render(request, 'apka/home.html', {'li':krok,'lang':lang,'globLang':globLang})

def editLan(request):
    global globLang
    globLang=request.POST.get('globLang')
    return HttpResponse("1")

def parser(request):
    piz=''
    if request.POST.get('url')==None:
        return render(request, 'apka/index.html', {'text': ""})
    text = ul.urlopen(request.POST.get('url')).read().decode('utf-8')
    text = BeautifulSoup(text)
    a=text.findAll('a',{'class':'left'})
    for A in a:
        if str(A.string)=='Посмотреть базу тестов':
            pages=['','?page=2','?page=3','?page=4']
            for i in pages:
                text=ul.urlopen(str(A['href'])+i).read().decode('utf-8')
                text=text.replace('</B>','')
                text=BeautifulSoup(text)
                tt=str(text.find('div',{'class','krok_title'}))

                langvege = Lang.objects.get(code='rus')
                bk=tt[tt.rfind('<br>')+4:tt.find('</br>')]
                cl=tt[tt.rfind('<small>')+7:tt.find('</small>')]
                try:
                    cl=Classes.objects.get(title=cl,lang=langvege)
                except Classes.DoesNotExist:
                    cl=Classes(title=cl,lang=langvege)
                    cl.save()
                try:
                    bk=Booklets.objects.get(title=bk,classes=cl,lang=langvege)
                except Booklets.DoesNotExist:
                    bk=Booklets(title=bk,classes=cl,lang=langvege)
                    bk.save()

                tables=text.findAll('table',{'class','question'})
                for table in tables:
                    que=str(table.findAll('div',{'class','question'}))
                    que=que[que.find('<div class="question">')+22:que.find('</div>')]
                    ans=table.findAll('div',{'class','new_answer'})
                    a=ans[0].contents[0].replace('A.','')
                    b=ans[1].contents[0].replace('B.','')
                    c=ans[2].contents[0].replace('C.','')
                    d=ans[3].contents[0].replace('D.','')
                    try:
                        e=ans[4].contents[0].replace('E.','')
                    except:
                        e="-"
                    z=Booklet(question=que,reply_1=a,reply_2=b,reply_3=c,reply_4=d,reply_5=e,booklet=bk)
                    z.save()




    return render(request, 'apka/index.html', {'text':request.POST.get('url')})

functoins={
    'start'

}

logging.basicConfig(
	level = logging.DEBUG,
	format = '%(asctime)s %(levelname)s %(message)s',
)
