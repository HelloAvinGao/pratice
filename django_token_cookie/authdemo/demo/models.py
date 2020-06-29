from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
class Register(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    mod_date = models.DateTimeField('Last modified', auto_now=True)
    age = models.IntegerField(blank=True)
    mobile = models.CharField(max_length=11, verbose_name=u"手机", null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default="image/2018/05/default_middile_2.png", max_length=100)
    gender = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')), default='female')
    address = models.CharField(max_length=100, blank=True)
    # blank=True表示admin后台可以为空
    #下面的__unicode__(self)方法，表示当输出这个类创建的对象时，默认会输出这个对象的name字段
    # def __unicode__(self):
    #     return self.name


