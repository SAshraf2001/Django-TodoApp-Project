from django.urls import path
from taskApp import views


urlpatterns = [
    path('task/', views.task_view, name='task'),
    path('update/<taskID>/', views.update_task, name='update_task'),
    path('delete/<taskID>/', views.delete_task, name='delete_task')
]