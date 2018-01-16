from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Spotifake.models import Music

"""HyperlinkedModelSerializer. """
"""You can also use primary key and various other relationships, but hyperlinking is good RESTful design."""


""" Albums """

""" Artistes """

""" Musiques """

class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('id', 'title')

""" Images """


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')