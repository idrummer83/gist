from django.db import models

# Create your models here.

from ckeditor.fields import RichTextField

class Snipet(models.Model):
    snipp_name = models.CharField('name', max_length=550, blank=True)
    language = models.CharField('language', max_length=255, default='', blank=True)
    code = models.TextField('code', blank=True)
    file = models.FileField('file', blank=True)
    link = models.CharField('link', max_length=1000, blank=True)
    visible = models.BooleanField('visibility', blank=True, default=True)

    class Meta:
        verbose_name = 'Snipet'
        verbose_name_plural = 'Snipet'