# формы для сайта

from .models import Task
from django.forms import ModelForm, Textarea, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]

        # todo: связать красоту бутстрапа с функционалом
        widgets = { 
            "title":TextInput(attrs={ 'class':'form-control', 'placeholder':'Имя задачи...' }),
            'task':Textarea(attrs={'class':'form-control', 'placeholder':'а по-подробнее?'}) 
        }