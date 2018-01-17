from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Spotifake.models import Album, Entertainer, Images, Music

"""HyperlinkedModelSerializer. """
"""You can also use primary key and various other relationships, but hyperlinking is good RESTful design."""


""" Albums """


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'album_name')


""" Artistes """


class EntertainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entertainer
        fields = ('id', 'stage_name')


""" Musiques """


class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('id', 'music_title')


""" Images """


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ('id', 'image_link')
