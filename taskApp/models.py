from django.db import models
from django.utils import timezone
from authApp.models import UserProfile

# Create your models here.
class Category(models.Model):
    catName = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.catName;

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"
        

class Task(models.Model):
    status_choices = {
        'isPending': 'Pending',
        'isCompleted': 'Completed',
        'inProgress': 'Progress'
    }
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='tasks')
    taskName = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=20, choices=status_choices, default='isPending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.taskName;