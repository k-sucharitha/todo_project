from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django .views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Task


# def taskList(request):
#     return HttpResponse('To Do List')


class TaskList(ListView):
    """Follow more for Class Based Views at https://dennisivy.com/django-class-based-views"""
    """template_name: By default the ListView Looks for a template with the prefix of the model name (task) and the suffix of _list.html if not otherwise set (task_list.html). 
    This can be overridden by setting the “template_name” attribute."""
    model = Task
    # template_name = 'base/task_list1.html'
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task 
    context_object_name = 'task'
    template_name = 'base/task_detail.html'


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')  


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task' 
    success_url = reverse_lazy('tasks') 


    


