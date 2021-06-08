from django.db import models
from django.utils import timezone


# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Hymn(models.Model):
    name = models.CharField(max_length=255)
    lyrics = models.CharField(max_length=25525)
    url = models.CharField(max_length=255)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)
    expired = models.DateTimeField()

    def __str__(self):
        return self.name
