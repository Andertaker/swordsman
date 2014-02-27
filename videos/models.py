# -*- coding: utf-8 -*-


from django.db import models
#from django.db.models import Model


#cmsplugin_filer_video
import settings
from django.utils.translation import ugettext_lazy as _
from filer.fields.file import FilerFileField
from os.path import basename



# Create your models here.
import datetime
from django.utils import timezone


#from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.core.context_processors import request
#from django.template import RequestContext
#from sekizai.context import SekizaiContext


class Category(models.Model):
    name = models.CharField('Название категории', max_length=100)
    slug = models.SlugField(unique=True)
    sort = models.PositiveSmallIntegerField('Порядок отображения', default=0, help_text="Элементы с меньшим значением следует первее")


    def __unicode__(self):
        return self.name

    class Meta:
        #name = ('event')
        verbose_name = ('Категория')
        verbose_name_plural = ('Категории')
        ordering = ['sort']
        permissions = (
            ("view_video", "Может просматривать видео альбомы"),
        )




class Album(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField('Название альбома', max_length=100)
    slug = models.SlugField(unique=True)
    sort = models.PositiveSmallIntegerField('Порядок отображения', default=0, help_text="Элементы с меньшим значением следует первее")
    
    description = models.TextField('Описание', blank=True)


    def __unicode__(self):
    	return self.name
 
    def videofiles_count(self):
        return self.videofiles_set.all().count()
    videofiles_count.short_description = 'Кол-во видео'
 

    class Meta:
        #name = ('event')
        verbose_name = ('Видео альбом')
        verbose_name_plural = ('Видео альбомы')
        ordering = ['sort']







class VideoFiles(models.Model):
    album = models.ForeignKey(Album)
    name = models.CharField('Название видео', max_length=100)
    
    
    # player settings
    movie = FilerFileField(verbose_name=_('movie file'), help_text=_('use .flv file or h264 encoded video file'), blank=True, null=True)
    movie_url = models.CharField(_('movie url'), max_length=255, help_text=_('vimeo or youtube video url. Example: http://www.youtube.com/watch?v=YFa59lK-kpo'), blank=True, null=True)


    
    description = models.TextField('Описание', blank=True)
    add_date = models.DateTimeField('Дата добавления', auto_now_add=True)    #auto_now_add=False


    width = settings.VIDEO_WIDTH
    height = settings.VIDEO_HEIGHT
    



    def __unicode__(self):
        if self.movie:
            name = self.movie.path
        else:
            name = self.movie_url
        return u"%s" % basename(name)

    def get_height(self):
        return "%s" % (self.height)
    
    def get_width(self):
        return "%s" % (self.width)    
    
    def get_movie(self):
        if self.movie:
            return self.movie.url
        else:
            return self.movie_url


    class Meta:
        #name = ('event')
        verbose_name = ('Видео файл')
        verbose_name_plural = ('Видео файлы')
        ordering = ['add_date']


    

    def render_video(self):
        #return render_to_response('videos/video.html', self)
        
        #context = RequestContext(request, {
        #    "object": self
        #})
        
        context = {'object': self}
        
        return render_to_string('videos/video.html', context)   #




    