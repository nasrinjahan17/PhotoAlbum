from django.contrib import admin
from .models import *
# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','category','image','date']

class CategoryAdmin(admin.ModelAdmin):
    list_display =['id','name']
    
admin.site.register(Photo,PhotoAdmin)
admin.site.register(Category,CategoryAdmin)