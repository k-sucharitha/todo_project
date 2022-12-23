from django.urls import path

from .views import (CustomLoginView, DeleteView, TaskCreate, TaskDetail,
                    TaskList, TaskUpdate, task_list)
from django.contrib.auth.views import LogoutView

urlpatterns = [
     path('login/', CustomLoginView.as_view(), name='login'),
     # path('logout/', LogoutView.as_view(template_name='base/logout.html'), name='logout'),
     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
     path('', TaskList.as_view(), name='tasks'), 
     # path('', task_list, name='tasks'), 
     path('task/<int:pk>/', TaskDetail.as_view(), name='task'), 
     path('task-create/', TaskCreate.as_view(), name='task-create'),
     path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
     path('task-delete/<int:pk>/',DeleteView.as_view(), name='task-delete'),

     
]    
  