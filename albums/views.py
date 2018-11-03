from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework import viewsets
from .models import Album, AlbumSerializer,Photo,PhotoSerializers
# Create your views here.


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers


def index(request):
    return render(request, 'index.html')


def details(request):
    return render(request, 'details.html')
