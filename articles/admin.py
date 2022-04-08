from dataclasses import fields
from pickle import READONLY_BUFFER
from re import search
from django.contrib import admin
from .models import Articles, Tag
# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
     list_display = ['id', 'tag']
class ArticleAdmin(admin.ModelAdmin):
     list_display = ['id','author', 'title', 'slug', 'content', 'last_update', 'created_at']
     search_fields = ['id', 'title', 'content']
     fields = ['author','title','image', 'slug','content','tags', 'time', 'last_update', 'created_at']
    # list_filter = ['created_at']
     readonly_fields = ['last_update', 'created_at']
     list_editable = ['title']
     prepopulated_fields = {'slug': ('title',)}
     filter_horizontal = ['tags', ]
     save_on_top = True
admin.site.register(Articles,ArticleAdmin)
