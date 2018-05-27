from django.db import models
from django.urls import reverse


GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]


class StudentData(models.Model):
    class Meta:
        app_label = 'student_account'


    FirstName = models.CharField(max_length=200, default='none')
    LastName = models.CharField(max_length=200, default='none')
    UserName = models.CharField(max_length=20, default='none')
    password = models.CharField(max_length=20, default='none')
    Gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default='Other')
    DoB = models.DateField(blank=True, null=True)
    HomeAddress = models.CharField(max_length=200, default='none')
    Email = models.CharField(max_length=200, default='none')
    pNumber = models.CharField(max_length=13, default='none')
    subjects = models.CharField(max_length=200, default='none')
    pFirstName = models.CharField(max_length=200, default='none')
    pLastName = models.CharField(max_length=200, default='none')
    parentsNumber = models.CharField(max_length=13, default='none')
    pEmail = models.CharField(max_length=200, default='none')

    def __str__(self):
        return self.FirstName
               # + (' - ') + self.LastName + (' - ') + self.GenderRadioOptions + (' - ') + self.DoB + (
            # ' - ') + self.HomeAddress + (' - ') + self.Email + (' - ') + self.pNumber

    def get_absolute_url(self):
        return reverse('student_account:student_account.html')
