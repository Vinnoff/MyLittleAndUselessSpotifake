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
    url(r'^entertainer/$', views.entertainer_list, name='entertainer-list'),
    url(r'^entertainer/(?P<pk>[0-9]+)/$', views.entertainer_detail, name='entertainer-detail')
]
