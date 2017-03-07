from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
import urllib.request as ul
from .models import Lang,Classes,Booklets,Booklet,Panel,bottomLang,Saveq,Errors,Content,Files
#from bs4 import BeautifulSoup
import logging
import json
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

def show(request,num=-1):
    linkPanel=Panel.objects.get(lang=lang2)
    content = Content.objects.get(lang=lang2)
    if num==-1:
        cl=Classes.objects.first()
        num=cl.id
    else:
        cl = Classes.objects.get(id=num)
    bl=Booklets.objects.filter(classes=cl,lang=lang2).order_by('id')
    bat=bottomLang.objects.get(lang=lang2)
    return render(request, 'apka/book.html', {'lang':lang,'globLang':globLang,'linkPanel':linkPanel,'num':"/"+str(num),
                                              'bl':bl,'bat':bat,'content':content,'titl':cl})
def login(request,num=1):
    content=Content.objects.get(lang=lang2)
    return render(request, 'apka/login.html', {'lang':lang,'globLang':globLang,'content':content})
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
        mass[-1]['id']=i.id
    return render(request, 'apka/tests/show.html', {'lang':lang,'globLang':globLang,'linkPanel':linkPanel,'num':"/"+str(numCl),
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
        mass[-1]['id']=i.id
    return render(request, 'apka/tests/training.html', {'lang':lang,'globLang':globLang,'linkPanel':linkPanel,'num':'/'+str(numCl),
                                                    'ran':range(10,200,10),
                                                    'tests':mass,'b':b})
def base(request,numCl,numB):
    linkPanel = Panel.objects.get(lang=lang2)
    b=get_object_or_404(Booklets,id=numB)
    mtest=Booklet.objects.filter(booklet=b)

    return render(request, 'apka/tests/base.html', {'lang':lang,'globLang':globLang,'linkPanel':linkPanel,'num':'/'+str(numCl),
                                                    'ran':range(10,200,10),
                                                    'tests':mtest,'b':b})
def errors(request):
    linkPanel = Panel.objects.get(lang=lang2)
    content = Content.objects.get(lang=lang2)
    if request.user.is_authenticated() and request.user.is_active:
        mtest=Errors.objects.filter(author=request.user)
        mass=[]
        for i in mtest:
            mass.append({'title':i.que.question,'m':[]})
            a=[{'r':i.que.reply_1,'c':'tr'},{'r':i.que.reply_2,'c':''},{'r':i.que.reply_3,'c':''},{'r':i.que.reply_4,'c':''},{'r':i.que.reply_5,'c':''}]
            shuffle(a)
            mass[-1]['m']=a
            mass[-1]['id']=i.id
    else:
        mass = []
    return render(request, 'apka/errors.html', {'lang':lang,'globLang':globLang,'linkPanel':linkPanel,'tests':mass,'content':content})

def save(request):
    linkPanel = Panel.objects.get(lang=lang2)
    content = Content.objects.get(lang=lang2)
    if request.user.is_authenticated() and request.user.is_active:
        mtest=Saveq.objects.filter(author=request.user)
        mass=[]
        for i in mtest:
            mass.append({'title':i.que.question,'m':[]})
            a=[{'r':i.que.reply_1,'c':'tr'},{'r':i.que.reply_2,'c':''},{'r':i.que.reply_3,'c':''},{'r':i.que.reply_4,'c':''},{'r':i.que.reply_5,'c':''}]
            shuffle(a)
            mass[-1]['m']=a
            mass[-1]['id']=i.id
    else:
        mass=[]
    return render(request, 'apka/save.html', {'lang':lang,'globLang':globLang,'linkPanel':linkPanel,'tests':mass,'content':content})

def download(request,numCl=-1):
    linkPanel = Panel.objects.get(lang=lang2)
    content = Content.objects.get(lang=lang2)
    if numCl==-1:
        cl=Classes.objects.first()
        num=cl.id
    else:
        cl=get_object_or_404(Classes,id=numCl)
    dow=Files.objects.filter(classes=cl,lang=lang2).order_by('-id')
    return render(request, 'apka/download.html', {'lang':lang,'globLang':globLang,'linkPanel':linkPanel,'content':content,'bl':dow})


def inspection(request):
    pakege=json.loads(request.POST.get('jsonData'))
    ans=[]
    for k in pakege:
        t=Booklet.objects.get(id=int(k))
        if t.reply_1!=pakege[k]:
            if request.user.is_authenticated() and request.user.is_active:
                try:
                    e = Errors.objects.get(author=request.user, que=t)
                except ObjectDoesNotExist:
                    e = Errors(author=request.user, que=t)
                    e.save()
            ans.append({})
            ans[-1]['title']=t.question
            ans[-1]['m']=[{'cl':'Tr','v':t.reply_1}]
            ans[-1]['m'].append({'cl':'fa','v':t.reply_2}) if   t.reply_2==pakege[k] else ans[-1]['m'].append({'cl':'','v':t.reply_2})
            ans[-1]['m'].append({'cl':'fa','v':t.reply_3}) if   t.reply_3==pakege[k] else ans[-1]['m'].append({'cl':'','v':t.reply_3})
            ans[-1]['m'].append({'cl':'fa','v':t.reply_4}) if   t.reply_4==pakege[k] else ans[-1]['m'].append({'cl':'','v':t.reply_4})
            ans[-1]['m'].append({'cl':'fa','v':t.reply_5}) if   t.reply_5==pakege[k] else ans[-1]['m'].append({'cl':'','v':t.reply_5})
            ans[-1]['id']=t.id
    try:
        mTrue=((len(pakege)-len(ans))/len(pakege))*100
    except ZeroDivisionError:
        mTrue=0
        mFalse = 0
    else:
        mFalse=100-mTrue
    return render(request, 'apka/tests/insp.html',{'tr':mTrue,'fa':mFalse,'ans':ans})

def star(request):
    if request.user.is_authenticated() and request.user.is_active and request.method == "POST":
        i=request.POST.get('id')
        try:
            q=Booklet.objects.get(id=i)
        except ObjectDoesNotExist:
            return HttpResponse('-1')
        try:
            s=Saveq.objects.get(author=request.user,que=q)
        except ObjectDoesNotExist:
            s=Saveq(author=request.user,que=q)
            s.save()
        return HttpResponse(i)
    else:
        return HttpResponse('-1')

def delError(request):
    if request.user.is_authenticated() and request.user.is_active and request.method == "POST":
        i=request.POST.get('id')
        e=Errors.objects.get(author=request.user,id=i)
        e.delete()
    return HttpResponse(i)

def delSave(request):
    if request.user.is_authenticated() and request.user.is_active and request.method == "POST":
        i=request.POST.get('id')
        e=Saveq.objects.get(author=request.user,id=i)
        e.delete()
    return HttpResponse(i)

def parser(request):
    piz=''
    if request.POST.get('url')==None:
        return render(request, 'apka/index.html', {'text': ""})
    text = ul.urlopen(request.POST.get('url')).read().decode('utf-8')
    text = BeautifulSoup(text)
    a=text.findAll('a',{'class':'left'})
    for A in a:
        if str(A.string)=='Переглянути базу тестів':
            pages=['','?page=2','?page=3','?page=4']
            for i in pages:
                text=ul.urlopen(str(A['href'])+i).read().decode('utf-8')
                text=text.replace('</B>','')
                text=text.replace('gSUP>+</SUP>','g+')
                text=text.replace('OSUP>-</SUP>','O-')
                text=BeautifulSoup(text)
                tt=str(text.find('div',{'class','krok_title'}))

                langvege = Lang.objects.get(code='ukr')
                bk=tt[tt.rfind('<br>')+4:tt.find('</br>')]
                cl=tt[tt.rfind('<small>')+7:tt.find('</small>')]
                cl=Classes.objects.get(id=37)
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
    l=Lang.objects.get(code='rus')
    cl=Classes.objects.get(id=36)
    massY=[i for i in range(2009,2014,1)]

    #massN=['01','02','04','05','06','07','08','09','20','22','24','29']
   # massN=['07','11','13','15','22','07','08','09','20','22','24','29']
    massN=['07','09','11','13','15','07','08','09','20','22','24','29']
    #massN=['06','07','08','10','11','12','13','14','15','17','19','29']
    for m in range(len(massY)):
        a=Files(classes=cl,lang=l,files='36/E07t'+str(massN[m])+"_11_"+str(massY[m])+'R.pdf')
        a.save()

    return render(request, 'apka/index.html', {})

logging.basicConfig(
	level = logging.DEBUG,
	format = '%(asctime)s %(levelname)s %(message)s',
)
