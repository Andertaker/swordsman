# -*- coding: utf-8 -*-
from django.contrib import admin

from django.contrib.auth.models import User
from training.models import Event, Score





class ScoreInline(admin.TabularInline):
    fields = ('user', 'score', 'comment')
    model = Score
    extra = 10
    ordering = ['user']


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(is_active=True).order_by("username")
        return super(ScoreInline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'users_count')

    inlines = [ScoreInline]



admin.site.register(Event, EventAdmin)




class ScoreAdmin(admin.ModelAdmin):
    fields = ['event', 'user', 'score', 'comment']
    list_display = ('event','user', 'score', 'comment')
    list_filter = ['user']

#admin.site.register(Score, ScoreAdmin)




