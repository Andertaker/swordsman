from django.conf.urls import patterns, url

from training import views



urlpatterns = patterns('',

    # ex: /photos/
    url(r'^$', views.ScoresView.as_view(), name='index'),
    url(r'^total_scores$', views.TotalScoresView.as_view(), name='total_scores'),
    
    url(r'^events$', views.EventsListView.as_view(), name='events'),
    url(r'^event/(?P<pk>\d+)$', views.EventDetailView.as_view(), name='event_detail'),
    # ex: /photos/5/
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

)