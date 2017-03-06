from django.db import models
from django.contrib.auth.models import User

class Lang(models.Model):
    title=models.CharField('прим. Українською мовою',max_length=100)
    img = models.CharField('сылка на картинку', max_length=100,null=True)
    code = models.CharField('Сокращенное название языка', max_length=100,null=True)
    def __str__(self):
        return str(self.title)

    class Meta:
            verbose_name = u'Язык'
            verbose_name_plural = u'Языки'

class Classes(models.Model):
    rus=models.CharField('Русский',max_length=300,null=True)
    ukr=models.CharField('Украинский',max_length=300,null=True)
    eng=models.CharField('Английский',max_length=300,null=True)
    def __str__(self):
        return str(self.id)+"."+str(self.rus)

    class Meta:
            verbose_name = u'Клас'
            verbose_name_plural = u'Класы(прим.КРОК 1 - Стоматология)'
    # связь с буклетами (1-М)




class Booklets(models.Model):
    title = models.CharField('Название буклета, прим. Буклет 2016 року', max_length=300)
    classes  = models.ForeignKey(Classes,on_delete=models.SET_NULL,null=True)
    lang  = models.ForeignKey(Lang,on_delete=models.PROTECT)
    def __str__(self):
        return str(self.title+'('+str(self.lang)+" / "+str(self.classes)+")")
    class Meta:
            verbose_name = u'Буклеты'
            verbose_name_plural = u'Буклеты'

class Booklet(models.Model):
    question=models.TextField('Вопрос')
    reply_1=models.CharField('Отввет_1',max_length=400)
    reply_2=models.CharField('Отввет_2',max_length=400)
    reply_3=models.CharField('Отввет_3',max_length=400)
    reply_4=models.CharField('Отввет_4',max_length=400)
    reply_5=models.CharField('Отввет_5',max_length=400)

    booklet=models.ForeignKey(Booklets,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
    class Meta:
            verbose_name = u'Вопросы - ответы'
            verbose_name_plural = u'Вопросы-ответы'



class Panel(models.Model):
    t1=models.CharField('ПРосмотр',max_length=300)
    t2=models.CharField('Скачать',max_length=300)
    t4=models.CharField('Ошибки',max_length=300)
    t5=models.CharField('Сохрі',max_length=300)

    lang = models.ForeignKey(Lang, on_delete=models.PROTECT,null=True)

class bottomLang(models.Model):
    t1=models.CharField('Розпочати тестування ',max_length=300)
    t2=models.CharField('Розповчати навчання',max_length=300)
    t3=models.CharField('Переглянути базу',max_length=300)
    lang = models.ForeignKey(Lang, on_delete=models.PROTECT, null=True)

class Saveq(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    que= models.OneToOneField(Booklet,on_delete=models.CASCADE)

class Errors(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    que = models.OneToOneField(Booklet, on_delete=models.CASCADE)


class Content(models.Model):
    lang = models.ForeignKey(Lang, on_delete=models.PROTECT, null=True)
    notone = models.CharField('Ни одного теста не найдено',max_length=500)
    error_1 = models.CharField('нет ошибок',max_length=500)
    error_2 = models.CharField('Зарегайся мразь',max_length=500)
    save_1 = models.CharField('Нихера не сохранил',max_length=500)
    save_2 = models.CharField('Войди сука шоб сохранять',max_length=500)
    notDown = models.CharField('Скачать', max_length=500, null=True)
    login = models.CharField('Зайди в соцсеть пидор',max_length=500)

class Files(models.Model):
    classes=models.ForeignKey(Classes,on_delete=models.PROTECT, null=True)
    files=models.CharField('путь',max_length=300)
    lang = models.ForeignKey(Lang, on_delete=models.PROTECT, null=True)
    def __str__(self):
        return str(self.files)