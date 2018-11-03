from django.db import models
from datetime import datetime
from rest_framework import serializers


class Album(models.Model):
    title = models.CharField(max_length=50, blank=False)
    owner = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=False)
    photo = models.ImageField(upload_to='albums/static/images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class PhotoSerializers(serializers.ModelSerializer):
    class Meta:
            model = Photo
            fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
            model = Album
            fields = '__all__'
