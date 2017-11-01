from django.db import models
from django.contrib import admin
from DjangoUeditor.models import UEditorField
# Create your models here.


#User
class User(models.Model):

    username = models.CharField(max_length=30, null=False, unique=True)
    email = models.CharField(max_length=30, null=False, unique=True)
    password = models.CharField(max_length=30, null=False)
    img = models.ImageField(null=True, upload_to='img')
    regist_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)


class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'img', 'last_login')


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'part'),
        ('p', 'published'),
    )

    title = models.CharField('标题', max_length=100)
    content = UEditorField('内容', width=1280, height=800, toolbars='full', imagePath='img_article/', filePath='newfile/')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    status = models.CharField('文章状态', choices=STATUS_CHOICES, max_length=1)
    abstract = UEditorField('内容', width=700, height=400, toolbars='full', imagePath='img_abstract/', filePath='newfile/')
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    top = models.BooleanField('置顶', default=False)
    category = models.ForeignKey('Category', verbose_name='分类',
                                 null=True, related_name='article',
                                 on_delete=models.SET_NULL,
                                 to_field='name')
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)

    class Meta:
        ordering = ['-create_time']


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'category', 'create_time', 'status')
    search_fields = ('title',)


class Category(models.Model):
    name = models.CharField('类名', max_length=20, unique=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('标签名', max_length=20, unique=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name


class Sign(models.Model):
    content = models.CharField('签名', max_length=200, unique=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)


class SignAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_time', 'update_time')

admin.site.register(User, UserAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Sign, SignAdmin)
admin.site.register(Category)
admin.site.register(Tag)

