from django.contrib import admin

from .models import ConvertTextModel, ConvertFileModel


# Register your models here.
admin.site.register(ConvertTextModel)
admin.site.register(ConvertFileModel)
