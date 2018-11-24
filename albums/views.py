from django.shortcuts import render, redirect
from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponseRedirect
from .permissions import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        response = super(AlbumViewSet, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='/')

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return Album.objects.all().filter(user=self.request.user)
        return None


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnlyPhoto,)

    def create(self, request, *args, **kwargs):
        response = super(PhotoViewSet, self).create(request, *args, **kwargs)
        if 'HTTP_REFERER' in request.META:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return response

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Photo.objects.filter(album__user=self.request.user)
            album_id = self.request.query_params.get('album', None)
            if album_id is not None:
                queryset = queryset.filter(album=album_id)
            return queryset
        return None

    def update(self, request, *args, **kwargs):
        print(request.data)
        instance = self.get_object()
        serializer = PhotoSerializers(instance, data={'keyword': request.data['keyword']}, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(**serializer.validated_data)
        response = Response(serializer.validated_data)
        return response


@csrf_exempt
@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@csrf_exempt
@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def shared_photo(request):
    file_name = request.GET.get('file_name')
    type = request.GET.get('type')
    photo_id = Photo.objects.get(photo__icontains=file_name).id

    context = {
        'photo_url': file_name + "." + type,
        'photo_id': photo_id
    }

    return render(request, 'shared-photo.html', context)