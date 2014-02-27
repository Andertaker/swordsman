# -*- coding: utf-8 -*-



from django.contrib import admin
from training.models import Event, Score



class ScoreInline(admin.TabularInline):
    fields = ('user', 'score', 'comment')
    model = Score
    extra = 10
    ordering = ['user']



class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'users_count')
    
    inlines = [ScoreInline]



admin.site.register(Event, EventAdmin)




class ScoreAdmin(admin.ModelAdmin):
    fields = ['event', 'user', 'score', 'comment']
    list_display = ('event','user', 'score', 'comment')
    list_filter = ['user']

#admin.site.register(Score, ScoreAdmin)




