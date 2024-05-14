from django.db import models

class Singer(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Song(models.Model):
    song_name = models.CharField(max_length=30)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='songs')
    duration = models.FloatField()

    def __str__(self):
        return self.song_name
