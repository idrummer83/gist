from django.db import models

# Create your models here.

class Base(models.Model):
    language = models.CharField('language', max_length=255, default='', blank=True)
    visible = models.BooleanField('visibility', blank=True, default=True)
    created = models.DateTimeField()
    def __str__(self):
        return "%s %s" % (self.created, self.language)


class UrlSnipet(models.Model):
    base = models.ForeignKey(Base, on_delete=models.CASCADE, null=True)
    file_url = models.CharField('file_url', max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = 'UrlSnipet'
        verbose_name_plural = 'UrlSnipet'


class FileSnipet(models.Model):
    base = models.ForeignKey(Base, on_delete=models.CASCADE, null=True)
    file = models.FileField('file', blank=True, null=True, upload_to='file')

    class Meta:
        verbose_name = 'FileSnipet'
        verbose_name_plural = 'FileSnipet'


class CodeSnipet(models.Model):
    base = models.ForeignKey(Base, on_delete=models.CASCADE, null=True)
    code = models.TextField('code', blank=True, null=True)

    class Meta:
        verbose_name = 'CodeSnipet'
        verbose_name_plural = 'CodeSnipet'