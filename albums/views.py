from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PhotoSerializers(instance, data={'keyword': request.data['keyword']}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(**serializer.validated_data)
        response = Response(serializer.validated_data)
        return response


@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def details(request):
    album_id = request.GET.get('album')
    context = {
        'album': album_id
    }

    album = Album.objects.get(id=album_id)
    if album:
        album_name = album.title
        context['album_name'] = album_name

    return render(request, 'details.html', context)