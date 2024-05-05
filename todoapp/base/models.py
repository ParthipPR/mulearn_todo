from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.

class Task(models.Model):
    contents = models.CharField(max_length=500)
    deadline = models.DateField('deadline')
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)