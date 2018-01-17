"""from django.shortcuts import render"""

# Create your views here.
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from Spotifake.serializers import MusicSerializer, ImageSerializer, EntertainerSerializer, AlbumSerializer
from Spotifake.models import Music, Images, Entertainer, Album
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError


""" Albums """


@csrf_exempt
def album_list(request):
    return list_methods(Album, AlbumSerializer, request)


@csrf_exempt
def album_detail(request, pk):
    return  detail_methods(Album, AlbumSerializer, request, pk)


""" Artistes """


@csrf_exempt
def entertainer_list(request):
    return list_methods(Entertainer, EntertainerSerializer, request)


@csrf_exempt
def entertainer_detail(request, pk):
    return  detail_methods(Entertainer, EntertainerSerializer, request, pk)


""" Musiques """


@csrf_exempt
def music_list(request):
    return list_methods(Music, MusicSerializer, request)


@csrf_exempt
def music_detail(request, pk):
    return detail_methods(Music, MusicSerializer, request, pk)


""" Images """


@csrf_exempt
def images_list(request):
    return list_methods(Images, ImageSerializer, request)


@csrf_exempt
def images_detail(request, pk):
    return detail_methods(Images, ImageSerializer, request, pk)


def list_methods(model, serial, request):
    if request.method == 'GET':
        all_object = model.objects.all()
        serializer = serial(all_object, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=400)
        serializer = serial(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


def detail_methods(model, serial, request, pk):
    try:
        selected_model = model.objects.get(pk=pk)
    except model.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serial(selected_model)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        serializer = serial(selected_model, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        selected_model.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)