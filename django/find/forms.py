from django import forms
from django.contrib.auth.models import User
from pages.models import *

class SearchBook(forms.Form):
    find_book = forms.CharField(label='Search with name or author:', max_length=100)
        

class AddNewBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_name', 'topic_name', 'publisher', 'publish_year', 'edition', )


class AddAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('author_name', )
