from django.shortcuts import render, redirect
from django.http import HttpResponse
from taskApp.models import Category, Task
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def task_view(request):
    if request.method == 'POST':
        taskName = request.POST['taskName']
        taskDescription = request.POST['taskDescription']
        taskCategory = request.POST['taskCategory']
        status = request.POST['taskStatus']
        catObject = Category.objects.get_or_create(catName=taskCategory, user=request.user)
        if catObject is not None:
            catObject = catObject[0]
            print(f'Cat Object is added into the Database: {catObject}')
            catObject.save();
        
        print(f'Cat Objects has been pushed {catObject.catName}')
        taskObject = Task.objects.create(taskName=taskName, category=catObject, user=request.user, taskDescription=taskDescription, status=status)
        if taskObject is not None: 
            print(f'Task Object is Saved into the Database: {taskObject}')
            messages.success(request, 'Task is saved successfully:' + taskObject.taskName)
            taskObject.save();
            return redirect('home')
        
    return render(request, 'taskApp/taskFlow_dashboard.html')


