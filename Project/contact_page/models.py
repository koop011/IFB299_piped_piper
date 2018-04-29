from django.db import models

# Create your models here.
from django import forms


class TeacherData(models.Model):
    FullName = models.CharField(max_length=200)
    DoB = models.CharField(max_length=20)
    HomeAddress = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    pNumber = models.CharField(max_length=13)
    certificates = models.CharField(max_length=200, default='none')
    subjects = models.CharField(max_length=200, default='none')

    def __str__(self):
        return self.FullName
