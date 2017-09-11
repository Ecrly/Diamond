from django import forms
from web.models import *

class NameForm(forms.Form):
    name = forms.CharField()


class TestUeditorModelForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
