from django.shortcuts import render
from rest_framework import viewsets
from rest_api.serializer import *
# Create your views here.

class UserViews(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class ImgViews(viewsets.ModelViewSet):

    queryset = ImageStore.objects.all()
    serializer_class = ImgSerializer
