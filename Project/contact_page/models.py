from django.db import models
from django.urls import reverse



class TeacherData(models.Model):

    # added in sprint 2
    class Meta:
        app_label = 'contact_page'


    fname = models.CharField(max_length=200, default='none')
    lname = models.CharField(max_length=200, default='none')
    DoB = models.CharField(max_length=20, default='none')
    HomeAddress = models.CharField(max_length=200, default='none')
    email = models.CharField(max_length=200, default='none')
    pNumber = models.CharField(max_length=13, default='none')
    certificates = models.CharField(max_length=200, default='none')
    # file = models.FileField(default='none')
    experience = models.CharField(max_length=200, default='none')
    reference = models.CharField(max_length=200, default='none')
    electric_guitar = models.BooleanField(default='False')
    guitar = models.BooleanField(default='False')
    keyboard = models.BooleanField(default='False')
    piano = models.BooleanField(default='False')
    drums = models.BooleanField(default='False')
    violin = models.BooleanField(default='False')
    saxophone = models.BooleanField(default='False')
    flute = models.BooleanField(default='False')
    cello = models.BooleanField(default='False')
    clarinet = models.BooleanField(default='False')


    def __str__(self):
        return self.fname + ' ' + self.lname

    def get_absolute_url(self):
        return reverse('contact_page:contact.html')

