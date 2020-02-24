from django.contrib import admin

# Register your models here.
from .models import WorldHeritageList, Site, State, Region, Category

admin.site.register(Site)
admin.site.register(State)
admin.site.register(Region)
admin.site.register(Category)
admin.site.register(WorldHeritageList)