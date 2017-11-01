from django import forms
from web.models import *

class NameForm(forms.Form):
    name = forms.CharField()


