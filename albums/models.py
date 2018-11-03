from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=50, blank=False)
    owner = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=False)
    photo = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
