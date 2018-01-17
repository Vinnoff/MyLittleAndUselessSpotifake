from django.db import models

# Create your models here.
""" Images """


class Images(models.Model):
    image_link = models.CharField(max_length=200)

    def __str__(self):
        return self.image_link


""" Artistes """


class Entertainer(models.Model):
    stage_name = models.CharField(max_length=200)
    entertainer_image = models.ForeignKey(Images, null=True, default=None, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.stage_name


""" Albums """


class Album(models.Model):
    album_name = models.CharField(max_length=200)
    entertainers = models.ManyToManyField(Entertainer)
    album_image = models.ForeignKey(Images, null=True, default=None, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name


""" Musiques """


class Music(models.Model):
    music_title = models.CharField(max_length=200)
    music_album = models.ForeignKey(Album, null=True, default=None, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.music_title
