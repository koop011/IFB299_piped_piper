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