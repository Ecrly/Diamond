from django.shortcuts import render

# Create your views here.

class MainPage(object):

    def index(request):
        return render(request, 'main/index.html')