from django.shortcuts import render
from django.views.generic.list import ListView
from django .views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

def task_list(request):
    queryset = Task.objects.all()
    return render(request, 'base/task_list.html', context={"tasks":queryset})


class TaskList(LoginRequiredMixin, ListView):
    """Follow more for Class Based Views at https://dennisivy.com/django-class-based-views"""
    """template_name: By default the ListView Looks for a template with the prefix of the model name (task) and the suffix of _list.html if not otherwise set (task_list.html). 
    This can be overridden by setting the “template_name” attribute."""
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task 
    context_object_name = 'task'
    template_name = 'base/task_detail.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # fields = '__all__'
    fields = ('title', 'description', 'complete',)
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form) 


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    # fields = '__all__'
    fields = ('title', 'description', 'complete',)
    success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task' 
    success_url = reverse_lazy('tasks') 


    


