from django import forms
from .models import Base, CodeSnipet, FileSnipet, UrlSnipet

class BaseForm(forms.ModelForm):

    class Meta:
        model = Base
        fields = ('language', 'visible')


class CodeSnipetForm(forms.ModelForm):

    class Meta:
        model = CodeSnipet
        fields = ('code',)



class FileSnipetForm(forms.ModelForm):

    class Meta:
        model = FileSnipet
        fields = ('file',)



class UrlSnipetForm(forms.ModelForm):

    class Meta:
        model = UrlSnipet
        fields = ('file_url',)