from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Task

# def taskList(request):
#     return HttpResponse('To Do List')


class TaskList(ListView):
    model = Task

