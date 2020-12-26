# здесь располагаются модели данных лабы

from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Название', max_length=50)   # заюзал charfield, поскольку 255 символов с лихвой хватит для названия
    task = models.TextField('Описание')

    # аннотация под строковый тип
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
