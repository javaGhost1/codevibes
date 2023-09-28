from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['blog']
    
