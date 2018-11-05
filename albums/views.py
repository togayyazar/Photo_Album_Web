from django.shortcuts import render
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from .models import Album, AlbumSerializer, Photo, PhotoSerializers
from django.http import HttpResponseRedirect


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def create(self, request, *args, **kwargs):
        response = super(AlbumViewSet, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='/')


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers

    def create(self, request, *args, **kwargs):
        response = super(PhotoViewSet, self).create(request, *args, **kwargs)
        if 'HTTP_REFERER' in request.META:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return response

    def get_queryset(self):
        queryset = Photo.objects.all()
        album_id = self.request.query_params.get('album', None)
        if album_id is not None:
            queryset = queryset.filter(album=album_id)
        return queryset

@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def details(request):
    album = request.GET.get('album')
    return render(request, 'details.html', {'album': album})