from django import forms
from django.contrib.auth.models import User
from pages.models import *
from mail.models import  *
class Mail(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text',)