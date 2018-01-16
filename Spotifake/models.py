from django.db import models

# Create your models here.
""" Albums """

""" Artistes """

""" Musiques """


class Music(models.Model):
    title = models.CharField(max_length=200)
    """album = models.ForeignKey(Album, on_delete=models.CASCADE)"""
    def __str__(self):
        return self.title


""" Images """
