# -*- coding: utf-8 -*-

from django.db import models

from django.contrib import admin
from models import *


from cms.plugin_pool import plugin_pool


from filer.fields.image import FilerImageField






#class VideoFilesInline(admin.TabularInline):
   # model = VideoFiles
   # extra = 1
    #fields = ("video_file")
    #list_display = ('video_file', 'name')
    
    #formfield_overrides = {
        #models.TextField: {'widget': text},
        #models.FileField: {'widget': VideoPluginPublisher},
    #}
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort')
    
admin.site.register(Category, CategoryAdmin)
    
    
    
    
    
    
    

class VideoFilesInline(admin.TabularInline):
    model = VideoFiles
    extra = 3

    fieldsets = [
        (None,               {'fields': ['name', 'movie', 'movie_url']}),
        #('Дата', {'fields': ['pub_date'], 'classes': ['collapse']}),        #
        ('Описание', {'fields': ['description'], 'classes': ['collapse']}),
    ]



class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['category']}),
        (None,               {'fields': ['name', 'slug', 'sort']}),
        #('Порядок следования', {'fields': ['sort']}),
        ('Описание', {'fields': ['description'], 'classes': ['collapse']}),
    ]

    inlines = [VideoFilesInline]


    list_display = ('name', 'sort', 'videofiles_count', 'category')  #


    #list_filter = ['pub_date']


    #date_hierarchy = 'pub_date'


admin.site.register(Album, AlbumAdmin)




class VideoFilesAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Альбом',               {'fields': ['album']}),
        (None,               {'fields': ['name', 'movie', 'movie_url']}),
        #('Дата', {'fields': ['pub_date'], 'classes': ['collapse']}),        #
        ('Описание', {'fields': ['description'], 'classes': ['collapse']}),
    ]
    
    list_display = ('__unicode__', 'name', 'add_date', 'album')
    
    list_filter = ['add_date']


admin.site.register(VideoFiles, VideoFilesAdmin)


