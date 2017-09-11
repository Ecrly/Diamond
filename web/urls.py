from django.conf.urls import url
from web.views import *


web_patterns = [
    url(r'^web/', MainPage.index, name='main'),
    url(r'^article/([\w\-.+@]+)/', ArticlePage.instance, name='article-instance'),
]
