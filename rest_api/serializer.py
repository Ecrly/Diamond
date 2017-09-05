from web.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class ImgSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageStore
        fields = '__all__'
