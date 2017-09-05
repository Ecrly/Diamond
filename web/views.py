from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.files.base import ContentFile
from web.models import *


class MainPage(object):

    @staticmethod
    def index(request):
        return render(request, 'main/index.html')


class Img(object):

    @staticmethod
    def img(request):
        s = request.FILES['image']
        if s == None:
            return HttpResponse('file not existing in the request')
        else:
            file_content = ContentFile(request.FILES['image'].read())
            img = ImageStore(name= request.FILES['image'].name, img=request.FILES['image'])
            img.save()
            return HttpResponse("en")
