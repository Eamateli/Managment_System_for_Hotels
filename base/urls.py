from django.urls import path 
from .views import TaskList, TaskDetails, TaskCrete, TaskUpdate, DeleteView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetails.as_view(), name='tasks'),
    path('task-create/', TaskCrete.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    
    

]