from django.db import models


# Create your models here.
class ConvertTextModel(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.text[0:16]} ...'


class ConvertFileModel(models.Model):
    file = models.FileField(upload_to='files/', blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.file.name}'
