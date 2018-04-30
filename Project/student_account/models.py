from django.db import models
from django.urls import reverse

GENDER_CHOICES= [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]

class StudentData(models.Model):
    FirstName = models.CharField(max_length=200, default='none')
    LastName = models.CharField(max_length=200, default='none')
    password = models.CharField(max_length=20, default='none')
    # GenderRadioOptions = models.ChoiceField(choices=GENDER_CHOICES)
    DoB = models.CharField(max_length=20, default='none')
    HomeAddress = models.CharField(max_length=200, default='none')
    Email = models.CharField(max_length=200, default='none')
    pNumber = models.CharField(max_length=13, default='none')
    subjects = models.CharField(max_length=200, default='none')

    def __str__(self):
        return self.FirstName

    def get_absolute_url(self):
        return reverse('student_account:student_account.html')