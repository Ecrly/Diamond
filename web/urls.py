from django.conf.urls import url
from web.views import *


web_patterns = [
    url(r'^web/', MainPage.index, name='web'),
    url(r'^article/([\w\-.+@]+)/', ArticlePage.instance, name='article-instance'),
    url(r'^archive/$', ArchivePage.list, name='archive'),
    url(r'^category/([\w\-.+@]+)/', ArchivePage.category, name='archive-category'),
    url(r'^tag/([\w\-.+@]+)/', ArchivePage.tag, name='archive-tag'),
]
