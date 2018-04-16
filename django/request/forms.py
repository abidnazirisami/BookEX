from django import forms
from django.contrib.auth.models import User
from pages.models import *
class SearchBook(forms.Form):
    find_book = forms.CharField(label='Search with name or author:', max_length=100)
        
