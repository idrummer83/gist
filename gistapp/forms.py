from django import forms

class Download(forms.Form):
    lang = forms.CharField(label='language', widget=forms.TextInput)
    code = forms.CharField(label='code', widget=forms.Textarea)
    file = forms.FileField(label='file', widget=forms.FileInput)
    link = forms.CharField(label='link', widget=forms.TextInput)