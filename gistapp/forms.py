from django import forms
from .models import Snipet


class Download(forms.ModelForm):

    class Meta:
        model = Snipet
        fields = ('language', 'code', 'file', 'link')
    # lang = forms.CharField(label='language', widget=forms.TextInput)
    # code = forms.CharField(label='code', widget=forms.Textarea)
    # file = forms.FileField(label='file', widget=forms.FileInput)
    # link = forms.CharField(label='link', widget=forms.TextInput)