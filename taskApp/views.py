from django.shortcuts import render
from django.http import HttpResponse
from taskApp.models import Category, Task
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def task_view(request):
    if request.method == 'POST':
        taskName = request.POST['taskName']
    return render(request, 'taskApp/taskFlow_dashboard.html')