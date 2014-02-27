from django.conf.urls import patterns, url


import views





urlpatterns = patterns('',

    # ex: /
    url(r'^$', views.CategoryIndexView.as_view(), name='category_list'),
    
    #  /category/white
    url(r'^category/(?P<slug>[\-\d\w]+)$', views.CategoryDetailView.as_view(), name='category_detail'),
    url(r'^album/(?P<slug>[\-\d\w]+)$', views.AlbumDetailView.as_view(), name='album_detail'),
        





)