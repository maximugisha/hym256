from django.db import models
from django.utils import timezone


# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=3)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField()

    def __str__(self):
        return self.name


class HymnNumber(models.Model):
    number = models.IntegerField(null=False, unique=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField()

    def __str__(self):
        return str(self.number)


class Hymn(models.Model):
    hymn_number = models.ForeignKey(HymnNumber, on_delete=models.CASCADE, related_name='hymn_number')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='hymn_language')
    title = models.CharField(max_length=255)
    lyrics = models.CharField(max_length=25525)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField()

    def __unicode__(self):
        return self.hymn_number


class HymnFile(models.Model):
    lyrics = models.ForeignKey(Hymn, on_delete=models.CASCADE, related_name='song_lyrics')
    url = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField()

    def __unicode__(self):
        return self.lyrics


class Ad(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=True)
    image_url = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField()
    expired = models.DateTimeField()

    def __str__(self):
        return self.name
