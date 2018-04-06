from django import forms
from django.contrib.auth.models import User
from pages.models import *

class AddBook(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('isbn',)

