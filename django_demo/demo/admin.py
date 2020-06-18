from django.contrib import admin
# from TestModel.models import Test
from demo.models import Test
from demo.models import Book
# Register your models here.
admin.site.register(Test)
admin.site.register(Book)