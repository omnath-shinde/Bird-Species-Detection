from django.contrib import admin
from .models import UserData

# Register your models here


class User(admin.ModelAdmin):
    list_display = ('name', 'image')


admin.site.register(UserData, User)
