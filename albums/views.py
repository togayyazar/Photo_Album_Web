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


@csrf_exempt
def index(request):
    return render(request, 'index.html')


def details(request):
    return render(request, 'details.html')
