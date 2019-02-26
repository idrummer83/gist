from django.db import models

# Create your models here.

from ckeditor.fields import RichTextField

class Post(models.Model):
    content = RichTextField(verbose_name='contenido')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'