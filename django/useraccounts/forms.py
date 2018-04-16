from django import forms
from django.contrib.auth.models import User
from pages.models import *

class EditProfile(forms.ModelForm):

    class Meta:
        model = OurUser
        fields = ('batch', 'roll','mail_id','phone','photo')

class EditUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name',)