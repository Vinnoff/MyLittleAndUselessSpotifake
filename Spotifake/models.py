from django.db import models

# Create your models here.
""" Albums """


class Album(models.Model):
    album_name = models.CharField(max_length=200)

    def __str__(self):
        return self.album_name


""" Artistes """


class Entertainer(models.Model):
    stage_name = models.CharField(max_length=200)

    def __str__(self):
        return self.stage_name


""" Musiques """


class Music(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


""" Images """


class Images(models.Model):
    image_link = models.CharField(max_length=200)

    def __str__(self):
        return self.image_link
