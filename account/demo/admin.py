from django.contrib import admin
from . import models
from django.contrib.auth.models import Group,User


# Register your models here.
# admin.site.unregister(Group)
# admin.site.unregister(User)
# admin.site.register(models.UserInfo)

admin.site.register(models.tableData)