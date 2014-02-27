from django.http import HttpResponse


from django.shortcuts import render, get_object_or_404
#from django.core.urlresolvers import reverse
from django.views import generic


from models import *






class CategoryIndexView(generic.ListView):
    model = Category
    #context_object_name = 'video_files'



class CategoryDetailView(generic.DetailView):
    model = Category
    slug_field = 'slug'
    


    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        category = self.get_object()
        context['albums'] = category.album_set.all()
        return context
    
    
    
class AlbumDetailView(generic.DetailView):
    model = Album
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(AlbumDetailView, self).get_context_data(**kwargs)
        album = self.get_object()
        context['videofiles'] = album.videofiles_set.all()
        return context
    
    
    
    
    
    
    


def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")



class VideoFilesView(generic.ListView):
    model = VideoFiles
    
    
    
    
class VideoFilesDetailView(generic.DetailView):
    model = VideoFiles
    #context_object_name = "file"
    #template_name = 'videos/video.html'
    #template_name = 'videos/video_html5.html'







class IndexViewBak(generic.ListView):
    template_name = 'videos/index.html'
    context_object_name = 'latest_albums_list'


    def get_queryset(self):
        """Return the last ten published albums."""
        return Album.objects.order_by('-pub_date')[:10]







    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        album = self.get_object()
        context['album_id'] = album.id
        #context['video_files'] = album.video_set.order_by('-add_date')[:10]
        

        
        
        return context

    template_name = 'videos/videos_detail.html'




class DetailViewBak(generic.DetailView):
    model = Album


    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        album = self.get_object()
        context['album_id'] = album.id
        context['videos'] = album.video_set.order_by('-add_date')[:10]
        
        
        context['embedvideo'] = album.embedvideo_set.order_by('-add_date')[:10]
        context['videothumbnail'] = album.videothumbnail_set.order_by('-add_date')[:10]

        
        
        return context

    template_name = 'videos/detail.html'


def detail(request, album_id):
    return HttpResponse("You're looking at poll %s." % album_id)

def photo(request, album_id):
    return HttpResponse("You're looking at the results of poll %s." % album_id)

def video(request, album_id):
    return HttpResponse("You're voting on poll %s." % album_id)









