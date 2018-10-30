from django.db import models
from datetime import datetime


class Album(models.Model):
    title = models.CharField(max_length=50, blank=False)
    owner = models.CharField(max_length=50, blank=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
