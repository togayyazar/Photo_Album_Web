from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from rest_framework import serializers
import uuid
import os
from photo_album import settings
from rest_framework.fields import CurrentUserDefault


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(settings.BASE_DIR, 'albums/static/images', filename)


class Album(models.Model):
    title = models.CharField(max_length=50, blank=False)
    user = models.ForeignKey(User, related_name='albums', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " - " + self.user.username


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=False, related_name='album')
    photo = models.ImageField(upload_to=get_file_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    keyword = models.CharField(max_length=20, blank=True)


class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
            model = Album
            fields = '__all__'


class PhotoSerializers(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super(PhotoSerializers, self).get_fields()
        fields['album'].queryset = Album.objects.filter(user=self.context['request'].user)
        return fields

    class Meta:
            model = Photo
            fields = '__all__'

