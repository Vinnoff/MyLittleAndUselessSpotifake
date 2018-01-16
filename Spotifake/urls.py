from sys import path

from django.conf.urls import url
from django.http import HttpResponse

from . import views

""" TODO A faire """
app_name = 'Spotifake'
urlpatterns = [
    url(r'^musics/$', views.music_list, name='music-list'),
    url(r'^musics/(?P<pk>[0-9]+)/$', views.music_detail, name='music-detail'),


]