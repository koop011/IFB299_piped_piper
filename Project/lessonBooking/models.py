from django.db import models
import datetime


# Create your models here.
class electric_guitar_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class keyboard_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class piano_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class guitar_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class drums_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class violin_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class saxophone_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class flute_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class cello_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class clarinet_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class electric_guitar_half_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class keyboard_half_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)


class piano_half_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class guitar_half_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class drums_half_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class violin_half_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class saxophone_half_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class flute_half_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class cello_half_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class clarinet_half_hour(models.Model):
    start_at = models.TimeField()
    def __str__(self):
        return str(self.start_at)

class pendingLessonContracts_new(models.Model):
    first_name = models.CharField(max_length=200, default='none')
    last_name = models.CharField(max_length=200, default='none')
    contract_period = models.CharField(max_length=10, default='none')
    instrument = models.CharField(max_length=200, default='none')
    time = models.CharField(default='none', max_length=20)
    day = models.CharField(default='none', max_length=20)
    timePeriod = models.CharField(default='none', max_length=20)

    def __str__(self):
        return self.first_name

class pendingLessonContracts_old(models.Model):
    first_name = models.CharField(max_length=200, default='none')
    last_name = models.CharField(max_length=200, default='none')
    contract_period = models.CharField(max_length=10, default='none')
    instrument = models.CharField(max_length=200, default='none')
    time1 = models.CharField(default='none', max_length=20)
    time2 = models.CharField(default='none', max_length=20)
    time3 = models.CharField(default='none', max_length=20)
    day1 = models.CharField(default='none', max_length=20)
    day2 = models.CharField(default='none', max_length=20)
    day3 = models.CharField(default='none', max_length=20)
    timePeriod1 = models.CharField(default='none', max_length=20)
    timePeriod2 = models.CharField(default='none', max_length=20)
    timePeriod3 = models.CharField(default='none', max_length=20)

    def __str__(self):
        return self.first_name



class days(models.Model):
    day = models.CharField(max_length=10, default='none')

    def __str__(self):
        return self.day

class period(models.Model):
    months=models.CharField(max_length=10, default='none')

    def __str__(self):
        return self.months