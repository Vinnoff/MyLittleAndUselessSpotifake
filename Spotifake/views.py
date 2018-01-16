"""from django.shortcuts import render"""

# Create your views here.
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from Spotifake.serializers import MusicSerializer, UserSerializer, GroupSerializer
from Spotifake.models import Music
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError



""" Albums """

""" Artistes """

""" Musiques """
@csrf_exempt
def music_list(request):
    if request.method == 'GET':
        musics = Music.objects.all()
        serializer = MusicSerializer(musics, many= True)
        return JsonResponse(serializer.data, safe=False, status= status.HTTP_200_OK)

    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status = 400)
        serializer = MusicSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse(status = status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def music_detail(request, pk):
    try:
        music = Music.objects.get(pk=pk)
    except Music.DoesNotExist:
        return HttpResponse(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return JsonResponse(serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status = status.HTTP_400_BAD_REQUEST)
        serializer = MusicSerializer(music, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status= status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        music.delete()
        return HttpResponse(status= status.HTTP_204_NO_CONTENT)

    else:
        return HttpResponse(status= status.HTTP_405_METHOD_NOT_ALLOWED)

""" Images """

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer