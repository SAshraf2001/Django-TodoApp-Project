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
        newTaskCat = request.POST['newCategory']
        taskStatus = request.POST['taskStatus']
        
        if newTaskCat != '':
            taskCategory = newTaskCat
        catObject = Category.objects.get_or_create(catName=taskCategory, user=request.user)
        if catObject is not None:
            catObject = catObject[0]
            # print(f'Cat Object is added into the Database: {catObject}')
            catObject.save();
        
        taskObject = Task.objects.create(taskName=taskName, category=catObject, user=request.user, taskDescription=taskDescription, status=taskStatus)
        if taskObject is not None: 
            # print(f'Task Object is Saved into the Database: {taskObject.status_choices}')
            messages.success(request, 'Task is saved successfully:' + taskObject.taskName)
            taskObject.save();
            return redirect('home')
        
    param = Task.objects.filter(user=request.user)
    # print(f'Task Object is Saved into the Database: {param}')
    paramCat = Category.objects.filter(user=request.user)
    statusChoices = Task.status_choices
    
    context = {
        'params': param,
        'catParams': paramCat,
        'statusChoices': statusChoices
    }
    # print(f'Cat Name has been seen: {paramCat[0].catName}')    
    return render(request, 'taskApp/taskFlow_dashboard.html', context)


@login_required 
def update_task(request, taskID):
    getContent = Task.objects.get(user=request.user, id=taskID)
    # return HttpResponse(f'Update Task: {getContent.taskName} with ID: {taskID}')
    if request.method == 'POST': 
        pass
    
    
@login_required
def delete_task(request, taskID):
    pass