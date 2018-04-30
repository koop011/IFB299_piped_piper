from django.db import models
from django.urls import reverse


class TeacherData(models.Model):
    FullName = models.CharField(max_length=200)
    DoB = models.CharField(max_length=20, default='none')
    HomeAddress = models.CharField(max_length=200, default='none')
    email = models.CharField(max_length=200, default='none')
    pNumber = models.CharField(max_length=13, default='none')
    certificates = models.CharField(max_length=200, default='none')
    subjects = models.CharField(max_length=200, default='none')

    def __str__(self):
        return self.FullName

    def get_absolute_url(self):
        return reverse('contact_page:contact.html')

