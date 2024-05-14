from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from .models import Singer,Song
from .serializer import SingerSerializer,SongSerializer



class SingerView(ListCreateAPIView):
    serializer_class=SingerSerializer
    queryset=Singer.objects.all()


class SongView(ListCreateAPIView):
    serializer_class=SongSerializer
    queryset=Song.objects.all()


