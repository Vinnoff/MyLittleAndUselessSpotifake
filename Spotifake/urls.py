from sys import path

from django.conf.urls import url
from django.http import HttpResponse

from . import views

""" TODO A faire """
app_name = 'Spotifake'
urlpatterns = [
    url(r'^musics/$', views.music_list, name='music-list'),
    url(r'^musics/(?P<pk>[0-9]+)/$', views.music_detail, name='music-detail'),
    url(r'^images/$', views.images_list, name='music-list'),
    url(r'^images/(?P<pk>[0-9]+)/$', views.images_detail, name='music-detail'),
    url(r'^entertainers/$', views.entertainer_list, name='entertainer-list'),
    url(r'^entertainers/(?P<pk>[0-9]+)/$', views.entertainer_detail, name='entertainer-detail'),
    url(r'^albums/$', views.album_list, name='album-list'),
    url(r'^albums/(?P<pk>[0-9]+)/$', views.album_detail, name='album-detail')
]
