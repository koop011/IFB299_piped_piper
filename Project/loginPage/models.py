from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class AccountManager(models.Model):
#     def create_account(self, title):
#         account = self.Create(title = title)
#         # do something?
#         return account


class Account(models.Model):
    title = models.CharField(max_length=20)
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    contactNumber = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, default='none')

    def __str__(self):
        return self.firstName + ' ' + self.lastName + ' - ' + self.userName
    #ainstrument = models.CharField(max_length=20)

    #objects = AccountManager()


class Student(models.Model):
    student = models.ForeignKey(Account, on_delete=models.CASCADE)
    #instrument = models.CharField(max_length=20)
