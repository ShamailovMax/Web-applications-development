# панель админа сайта

from django.contrib import admin
from .models import Task

# Register your models here.

admin.site.register(Task)
