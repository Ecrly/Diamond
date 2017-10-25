from django.shortcuts import render
from django.core.files.base import ContentFile
from web.models import *
from web.forms import *


# give the sign's number to create the random during (0, num)
sign_list = Sign.objects.all()
num = sign_list.count()


class MainPage(object):

    @staticmethod
    def index(request):
        article_list = Article.objects.filter(status='p')

        return render(request, 'main/index.html', {'article_list': article_list, 'sign_num': num})


class ArticlePage(object):

    @staticmethod
    def instance(request, article_id):

        context={}
        context['sign_num'] = num
        # get the article what we want to see and the before, after also
        article = Article.objects.get(id=article_id)
        # tags = []
        # for tag_id in article.tags.all():
        #     tag = Tag.objects.get(id=tag_id)
        #     tags.append(tag)
        # article.tags = tags
        context['article'] = article
        article_before = Article.objects.filter(id=(int(article_id)-1))
        if article_before.exists():
            print(article_before[0].title)
            context['article_before'] = article_before[0]
        else:
            print('before is null')
            context['article_before'] = None
        article_after = Article.objects.filter(id=(int(article_id)+1))
        if article_after.exists():
            print(article_after[0].title)
            context['article_after'] = article_after[0]
        else:
            print('after is null')
            context['article_after'] = None
        # when click to see the detail, make the views to add one
        # but when we refresh, the views also add
        article.views += 1
        article.save()

        return render(request, 'article/instance.html', context)


class ArchivePage(object):

    @staticmethod
    def list(request):

        # the abstract of category
        category_list = []
        categorys = Category.objects.all()
        for category in categorys:
            article_in = Article.objects.filter(category=category.name)
            category_info = { 'name': category.name, 'count': article_in.count()}
            category_list.append(category_info)

        # the abstract of tag
        tag_list = []
        tags = Tag.objects.all()
        for tag in tags:
            article_in = Article.objects.filter(tags=tag.id)
            category_info = {'name': tag.name, 'count': article_in.count(), 'id': tag.id}
            tag_list.append(category_info)

        article_list = Article.objects.all()
        return render(request, 'archive/archive.html', {'category_list': category_list, 'tag_list': tag_list, 'article_list': article_list, 'sign_num': num})

    @staticmethod
    def category(request, category_name):
        article_list = Article.objects.filter(category=category_name)
        info_before = category_name + '分类下的文章'
        return render(request, 'main/index.html', {'info_before': info_before, 'article_list': article_list, 'sign_num': num})

    @staticmethod
    def tag(request, tag_id):
        article_list = Article.objects.filter(tags=tag_id)
        tag = Tag.objects.get(id=tag_id)
        info_before = tag.name + '标签下的文章'
        return render(request, 'main/index.html',
                      {'info_before': info_before, 'article_list': article_list, 'sign_num': num})