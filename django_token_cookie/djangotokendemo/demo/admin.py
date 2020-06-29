from django.contrib import admin
from demo.models import message

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['username','password'] # list
    search_fields = ('username',)


admin.site.register(message,ContactAdmin)

