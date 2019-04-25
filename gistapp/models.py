from django.db import models

# Create your models here.

class Snipet(models.Model):
    snipp_name = models.CharField('name', max_length=550, blank=True)
    language = models.CharField('language', max_length=255, default='', blank=True)
    code = models.TextField('code', blank=True)
    # file = FilerFileField(null=True, blank=True, related_name="code_file", on_delete=models.CASCADE)
    file = models.FileField('file', blank=True, upload_to='file')
    visible = models.BooleanField('visibility', blank=True, default=True)
    created = models.DateTimeField()
    file_url = models.CharField('file_url', max_length=1000, blank=True)

    class Meta:
        verbose_name = 'Snippet'
        verbose_name_plural = 'Snippets'