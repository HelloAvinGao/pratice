from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=256)
    password = models.TextField(max_length=32)
    permissions = models.TextField(blank=True, null=True, verbose_name='permissions')
    email = models.EmailField(max_length=32)
    class Meta:
        default_permissions = ()

        permissions = (
            ("admin", "manager the page"),
            ("manager", "manager the project"),
            ("personal", "personal"),
        )
from django.forms import FilePathField


class tableData(models.Model):
    thName = models.CharField(max_length=10000)
    tableName = models.CharField(max_length=32,primary_key=True)
    TD_data = models.CharField(max_length=1000000)
    class Meta:
        ordering = ['tableName']


