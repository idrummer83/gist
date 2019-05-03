from django import forms
from .models import Snipet

class Download(forms.ModelForm):

    class Meta:
        model = Snipet
        fields = ('snipp_name', 'language', 'code', 'file', 'visible')
    # lang = forms.CharField(label='language', widget=forms.TextInput)
    # code = forms.CharField(label='code', widget=forms.Textarea)
    # file = forms.FileField(label='file', widget=forms.FileInput)