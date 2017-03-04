from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import urllib.request as ul
from .models import Lang,Classes,Booklets,Booklet,Panel,bottomLang
from bs4 import BeautifulSoup
import logging
from random import shuffle

globLang='ukr'
lang = Lang.objects.all()
lang2 = Lang.objects.get(code=globLang)
def start(request):

    krok=Classes.objects.all()

    return render(request, 'apka/home.html', {'li':krok,'lang':lang,'globLang':globLang})

def editLan(request):
    global globLang
    global lang2

    globLang=request.POST.get('globLang')
    lang2 = Lang.objects.get(code=globLang)
    return HttpResponse("1")

def show(request,num=1):
    linkPanel=Panel.objects.get(lang=lang2)
    cl=get_object_or_404(Classes,id=num)
    bl=Booklets.objects.filter(classes=cl,lang=lang2).order_by('id')
    bat=bottomLang.objects.get(lang=lang2)
    return render(request, 'apka/book.html', {'lang':lang,'globLang':globLang,'linkPanel':linkPanel,'num':num,
                                              'bl':bl,'bat':bat})
def login(request,num=1):

    return render(request, 'apka/login.html', {'lang':lang,'globLang':globLang})
def tests(request,numCl,numB):
    linkPanel = Panel.objects.get(lang=lang2)
    b=get_object_or_404(Booklets,id=numB)
    mtest=Booklet.objects.filter(booklet=b)
    mass=[]
    for i in mtest:
        mass.append({'title':i.question,'m':[]})
        a=[i.reply_1,i.reply_2,i.reply_3,i.reply_4,i.reply_5]
        shuffle(a)
        mass[-1]['m']=a
    return render(request, 'apka/tests/show.html', {'lang':lang,'globLang':globLang,'linkPanel':linkPanel,'num':numCl,
                                                    'ran':range(10,200,10),
                                                    'tests':mass,'b':b})
def training(request,numCl,numB):
    linkPanel = Panel.objects.get(lang=lang2)
    b=get_object_or_404(Booklets,id=numB)
    mtest=Booklet.objects.filter(booklet=b)
    mass=[]
    for i in mtest:
        mass.append({'title':i.question,'m':[]})
        a=[{'r':i.reply_1,'c':'tr'},{'r':i.reply_2,'c':''},{'r':i.reply_3,'c':''},{'r':i.reply_4,'c':''},{'r':i.reply_5,'c':''}]
        shuffle(a)
        mass[-1]['m']=a
    return render(request, 'apka/tests/training.html', {'lang':lang,'globLang':globLang,'linkPanel':linkPanel,'num':numCl,
                                                    'ran':range(10,200,10),
                                                    'tests':mass,'b':b})
def base(request,numCl,numB):
    linkPanel = Panel.objects.get(lang=lang2)
    b=get_object_or_404(Booklets,id=numB)
    mtest=Booklet.objects.filter(booklet=b)
    return render(request, 'apka/tests/base.html', {'lang':lang,'globLang':globLang,'linkPanel':linkPanel,'num':numCl,
                                                    'ran':range(10,200,10),
                                                    'tests':mtest,'b':b})


def parser(request):
    piz=''
    if request.POST.get('url')==None:
        return render(request, 'apka/index.html', {'text': ""})
    text = ul.urlopen(request.POST.get('url')).read().decode('utf-8')
    text = BeautifulSoup(text)
    a=text.findAll('a',{'class':'left'})
    for A in a:
        if str(A.string)=='Show base':
            pages=['','?page=2','?page=3','?page=4']
            for i in pages:
                text=ul.urlopen(str(A['href'])+i).read().decode('utf-8')
                text=text.replace('</B>','')
                text=text.replace('gSUP>+</SUP>','g+')
                text=text.replace('OSUP>-</SUP>','O-')
                text=BeautifulSoup(text)
                tt=str(text.find('div',{'class','krok_title'}))

                langvege = Lang.objects.get(code='eng')
                bk=tt[tt.rfind('<br>')+4:tt.find('</br>')]
                cl=tt[tt.rfind('<small>')+7:tt.find('</small>')]
                cl=Classes.objects.get(id=30)
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
                    a=str(ans[0])[str(ans[0]).find('</td><td>')+9:str(ans[0]).find('</td></tr>')]
                    b=str(ans[1])[str(ans[1]).find('</td><td>')+9:str(ans[1]).find('</td></tr>')]
                    c=str(ans[2])[str(ans[2]).find('</td><td>')+9:str(ans[2]).find('</td></tr>')]
                    d=str(ans[3])[str(ans[3]).find('</td><td>')+9:str(ans[3]).find('</td></tr>')]
                    a=a.replace('ss="new_answer" style="font-weight:bold;">','')
                    b=b.replace('ss="new_answer" style="">','')
                    c=c.replace('ss="new_answer" style="">','')
                    d=d.replace('ss="new_answer" style="">','')

                    a=a.replace('</div','')
                    b=b.replace('</div','')
                    c=c.replace('</div','')
                    d=d.replace('</div','')

                    a=a.replace('A.','')
                    b=b.replace('B.','')
                    c=c.replace('C.','')
                    d=d.replace('D.','')

                    a=a.strip()
                    b=b.strip()
                    c=c.strip()
                    d=d.strip()

                  #  d=ans[3].contents[0].replace('D.','')
                    try:
                        e = str(ans[4])[str(ans[4]).find('</td><td>') + 9:str(ans[4]).find('</td></tr>')]
                        e = e.replace('ss="new_answer" style="">', '')
                        e = e.replace('E.', '')
                        e = e.replace('</div', '')
                        e = e.strip()
                    except:
                        e="-"
                    z=Booklet(question=que,reply_1=a,reply_2=b,reply_3=c,reply_4=d,reply_5=e,booklet=bk)
                    z.save()




    return render(request, 'apka/index.html', {'text':request.POST.get('url')})


def abcc(request):
    b=Booklet.objects.all()[37000:]
    for i in b:
        i.reply_1=i.reply_1.strip()
        i.reply_2=i.reply_2.strip()
        i.reply_3=i.reply_3.strip()
        i.reply_4=i.reply_4.strip()
        i.reply_5=i.reply_5.strip()
        i.save()

    return render(request, 'apka/index.html', {})

logging.basicConfig(
	level = logging.DEBUG,
	format = '%(asctime)s %(levelname)s %(message)s',
)
