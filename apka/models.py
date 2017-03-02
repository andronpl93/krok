from django.db import models

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
    title=models.CharField('Название класа, прим. КРОК 1 - атология',max_length=300)
    lang = models.ForeignKey(Lang, on_delete=models.PROTECT,null=True)
    def __str__(self):
        return str(self.title)

    class Meta:
            verbose_name = u'Клас'
            verbose_name_plural = u'Класы(прим.КРОК 1 - Стоматология)'
    # связь с буклетами (1-М)




class Booklets(models.Model):
    title = models.CharField('Название буклета, прим. Буклет 2016 року', max_length=300)
    classes  = models.ForeignKey(Classes,on_delete=models.CASCADE)
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



