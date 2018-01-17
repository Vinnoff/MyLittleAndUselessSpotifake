from django.db import models

# Create your models here.
""" Albums """

""" Artistes """

""" Musiques """


class Music(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


""" Images """


class Images(models.Model):
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.link
