from django.db import models

# Create your models here.
class Test(models.Model):
    name   = models.CharField(max_length=200)
    age    = models.IntegerField(default=0)
    email  = models.EmailField()
    def __unicode__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(null=True, blank=True, max_length=30)
    author = models.CharField(null=True, blank=True, max_length=50)
    intro = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title