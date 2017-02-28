from django.shortcuts import render
import urllib.request as ul
from .models import Lang,Classes,Booklets,Booklet
from bs4 import BeautifulSoup

def start(request):
    return render(request, 'apka/index.html', {})
def parser(request):
    text=ul.urlopen(request.POST.get('url')).read().decode('utf-8')
    text=text.replace('</B>','')
    text=BeautifulSoup(text)
    tt=str(text.find('div',{'class','krok_title'}))

    langvege = Lang.objects.get(title='Українською мовою')
    bk=tt[tt.rfind('<br>')+4:tt.find('</br>')]
    cl=tt[tt.rfind('<small>')+7:tt.find('</small>')]
    try:
        cl=Classes.objects.get(title=cl)
    except Classes.DoesNotExist:
        cl=Classes(title=cl)
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
        e=ans[4].contents[0].replace('E.','')
        z=Booklet(question=que,reply_1=a,reply_2=b,reply_3=c,reply_4=d,reply_5=e,booklet=bk)
        z.save()




    return render(request, 'apka/index.html', {'text':""})

