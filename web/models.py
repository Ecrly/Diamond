from django.db import models
from django.contrib import admin
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

class ImageStore(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='image')

admin.site.register(User, UserAdmin)


