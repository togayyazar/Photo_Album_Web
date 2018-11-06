from django.db import models
from datetime import datetime
from rest_framework import serializers
import uuid
import os
from photo_album import settings


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(settings.BASE_DIR, 'albums/static/images', filename)


class Album(models.Model):
    title = models.CharField(max_length=50, blank=False)
    owner = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=False)
    photo = models.ImageField(upload_to=get_file_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    keyword = models.CharField(max_length=20, blank=True)


class PhotoSerializers(serializers.ModelSerializer):
    class Meta:
            model = Photo
            fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
            model = Album
            fields = '__all__'
