# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User

#import pprint

import datetime
#from django.utils import timezone






class Event(models.Model):
    name =  models.CharField('Событие', max_length=100)

    date = models.DateField('Дата события')	#, auto_now_add=True
    #limit_choices_to = {'date__lte': datetime.date.today}

    class Meta:
        #name = ('event')
        verbose_name = ('соревнование(событие)')
        verbose_name_plural = ('соревнования(события)')
        ordering = ['date']
        permissions = (
            ("view_statistic", "Может просматривать статистику"),
        )

    

    def __unicode__(self):
        return self.name

    def users_count(self):
        return self.score_set.all().count()
    users_count.short_description = 'Кол-во участников'




class Score(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(User)
    score = models.SmallIntegerField('Баллы')
    comment = models.CharField('Коментарий', blank=True, max_length=100)
    
    
    
    #def __unicode__(self):
        #return `self.event_id` + ' - ' + `self.user_id` + ' - ' + `self.score`
    
    
    class Meta:
        verbose_name = ('результат')
        verbose_name_plural = ('результаты')
        unique_together = ("event", "user")
    
    
    
    




