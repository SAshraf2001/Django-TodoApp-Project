from django.shortcuts import render
from django.http import HttpResponse
from taskApp.models import Category, Task
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def task_view(request):
    if request.method == 'POST':
        taskName = request.POST['taskName']
        taskDescription = request.POST['taskDescription']
        taskCategory = request.POST['taskCategory']
        status = request.POST['taskStatus']
        catObject = Category.objects.create(catName=taskCategory, user=request.user.UserProfile)
        taskObject = Task.objects.create(taskName=taskName, category=catObject, user=request.user.UserProfile, taskDescription=taskDescription, status=status)
        if taskObject is not None: 
            print(f'Task Object is Saved into the Database: {taskObject}')
            taskObject.save();
        
    return render(request, 'taskApp/taskFlow_dashboard.html')