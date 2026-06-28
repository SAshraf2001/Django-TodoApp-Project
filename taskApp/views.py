from django.shortcuts import render
from django.http import HttpResponse
from taskApp.models import Category, Task
from django.contrib.auth.decorators import login_required

# Create your views here.

def task_view(request):
    return HttpResponse('This is the testing of the Task Page:')