from django.shortcuts import render
from rest_framework import viewsets
from rest_api.serializer import *
# Create your views here.


class UserViews(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleView(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class SignView(viewsets.ModelViewSet):
    queryset = Sign.objects.all()
    serializer_class = SignSerializer