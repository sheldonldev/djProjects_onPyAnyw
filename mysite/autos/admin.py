from django.contrib import admin

from .models import MakeUser, AutoUser

# Register your models here.

admin.site.register(MakeUser)
admin.site.register(AutoUser)