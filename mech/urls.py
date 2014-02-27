# -*- coding: utf-8 -*-

from django.conf.urls.defaults import include
from django.conf.urls import patterns, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from reg_backend.views import RegistrationViewUniqueEmail







urlpatterns = patterns('',
    (r'^statistic/',  include('training.urls', namespace='statistic')),
    (r'^video/',  include('videos.urls', namespace="video")),
    (r'^photologue/', include('photologue.urls')),


    (r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/', include('registration.urls')),
    
    url(r'^register/$', RegistrationViewUniqueEmail.as_view(), name='registration_register'),
    #url(r'^register/complete/$',
    #                       TemplateView.as_view(template_name='registration/registration_complete.html'),
     #                      name='registration_complete'),
    
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    #url(r'^logout/$', views.user_logout, {'next_page': '/'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),


    url(r'^', include('cms.urls')),
)






if settings.DEBUG:
    urlpatterns = patterns('',
                           
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),     
                                  
    url(r'', include('django.contrib.staticfiles.urls')),
    
) + urlpatterns








