from django.db import models

# Create your models here.

from ckeditor.fields import RichTextField

class Snipet(models.Model):
    language = models.CharField('language', max_length=255, default='', blank=True)
    code = models.TextField('code')
    file = models.CharField('file', max_length=1000)
    link = models.CharField('link', max_length=1000)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'