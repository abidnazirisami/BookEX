from django import forms

class UploadFileForm(forms.Form):
    Photo = forms.ImageField(required=False)