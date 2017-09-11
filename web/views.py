from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.files.base import ContentFile
from web.models import *
from web.forms import *
import markdown


class MainPage(object):

    @staticmethod
    def index(request):
        # form = TestUeditorModelForm()
        article_list = Article.objects.filter(status='p')
        return render(request, 'main/index.html', {'article_list': article_list})

    @staticmethod
    def show(request):
        return render(request, 'article/instance.html')


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


class ArticlePage(object):

    @staticmethod
    def instance(request, ariticle_id):
        article = Article.objects.filter(id=ariticle_id)
        return render(request, 'article/instance.html', {'article': article[0]})
