# -*- coding: utf-8 -*-
import json
import copy
from datetime import datetime, timedelta

from django.views import generic
from django.db import connection, transaction
from django.contrib.auth.models import User

from training.models import Event, Score



def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]




class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'training/event_detail.html'
    context_object_name = 'event'


class EventsListView(generic.ListView):
    context_object_name = 'latest_events'
    
    def get_queryset(self):
        """За последние полгода"""
        date_from = datetime.now() - timedelta(days=180)
        return Event.objects.order_by('date').filter(date__gt=date_from)



class ScoresView(generic.TemplateView):
    template_name = 'training/index.html'
    #context_object_name = 'latest_contests_list'

        
    def get_context_data(self, **kwargs):
        context = super(ScoresView, self).get_context_data(**kwargs)
       
        "Берём точку отсчёта(тренировку) после которой выводим остальные"
        now = datetime.now()
        date_from = datetime.now() - timedelta(days=180)
        events = Event.objects.order_by('date').filter(date__gt=date_from)
        
        dates = []
        events_order = {}
        
        if not events:
            context['dates'] = '[]'
            context['series'] = '[]'
            return context

        i = 0;
        for e in events:
            dates.append(e.date.strftime("%d.%m.%Y"))
            events_order[e.id] = i
            i = i + 1

        cursor = connection.cursor()
        cursor.execute('''
            SELECT 
                --user_id,
                CONCAT(auth_user.last_name, ' ', auth_user.first_name) as name,
                GROUP_CONCAT(event_id) as events,
                GROUP_CONCAT(score) as scores
                
            FROM training_score
            LEFT JOIN auth_user ON (training_score.user_id = auth_user.id)
            WHERE auth_user.is_active AND training_score.event_id > %(event_id)s
            
            GROUP BY user_id
                ''', {"event_id": events[0].id})
                    
       
        series = []
        for r in dictfetchall(cursor):
            events = r["events"].split(",")
            scores = r["scores"].split(",")
            events = map(int, events)
            scores = map(int, scores)
            
            scores = dict(zip(events, scores))
            data = []
            
            total_score = 0
            for ev_id, i in events_order.iteritems():
                if ev_id in scores:
                    total_score += scores[ev_id]
                    data.append([i, total_score])

        
            series.append({"name": r["name"], "data": data})
        

        context['dates'] = json.dumps(dates)
        context['series'] = json.dumps(series)
        return context
        
    
    
    
class TotalScoresView(generic.ListView):
    template_name = 'training/total_scores.html'
    context_object_name = 'users'
    
    def queryset(self, **kwargs):
        qs = User.objects.raw('''
            SELECT 
                auth_user.id,
                COUNT(training_score.id) as training_count,
                SUM(training_score.score) as total_scores
                
            FROM auth_user
            LEFT JOIN training_score ON (training_score.user_id = auth_user.id)
            WHERE auth_user.is_active
            
            GROUP BY user_id
            HAVING total_scores IS NOT NULL
            ORDER BY auth_user.last_name
                ''')

        return qs

    
    
    
    
    
'''
SELECT 
    user_id,
    GROUP_CONCAT(event_id) as events_ids,
    GROUP_CONCAT(score) as scores
FROM training_score

GROUP BY user_id



SELECT 
    user_id,
    auth_user.last_name, auth_user.first_name,
                
                GROUP_CONCAT(
                    CONCAT(event_id, ': ', score)
                ) as series,
                
    
    GROUP_CONCAT(event_id) as events,
    GROUP_CONCAT(score) as scores
    
FROM training_score
LEFT  JOIN auth_user ON (training_score.user_id = auth_user.id)
WHERE auth_user.is_active


GROUP BY user_id



'''
    
'''
SELECT 
    event_id,
    GROUP_CONCAT(user_id) as user_ids,
    GROUP_CONCAT(score) as scores
FROM training_score

GROUP BY event_id

'''
    
    
    
    
    

    
