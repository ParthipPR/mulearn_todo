from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class Tasks(models.Model):
    contents = models.CharField(max_length=500)
    deadline = models.DateField('deadline')
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)