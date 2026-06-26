from django.db import models
from django.contrib.auth.models import AbstractUser
# Creating the Models for the Authentication of TodoApp...
class UserProfile(AbstractUser):
    contactNumber = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    REQUIRED_FIELDS = ['contactNumber', 'password']
    def __str__(self):
        return self.contactNumber;   