from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.exam)
admin.site.register(models.question)
admin.site.register(models.answers)
