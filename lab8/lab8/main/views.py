from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    tasks = Task.objects.order_by('-id')    # найти все объекты
    return render(request, 'main/index.html', {'title':'Главная страница сайта', 'tasks':tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):

    authorisationError = ''

    # *это чтобы отправить и сохранить задание 
    if request.method == 'POST':
        form = TaskForm(request.POST)

        # !!! проверка на правильность ввода данныхх
        if form.is_valid():
            form.save()                    # * и тогда сохраняем в БД нашей )0)
            return redirect('home')        # * скинули пользователя на главную...
        else:
            authorisationError = 'Неверная форма'

    form = TaskForm()
    context = { 'form':form, 'error':authorisationError }
    return render(request, 'main/create.html', context)
