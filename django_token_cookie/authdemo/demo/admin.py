from django.contrib import admin
from demo.models import Register
# Register your models here.
@admin.register(Register)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password')
    search_fields=('username',)               #指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    list_filter = ('id',)
