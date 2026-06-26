from django.urls import path
from taskApp import views


urlpatterns = [
    path('task/', views.task_view, name='task')
]