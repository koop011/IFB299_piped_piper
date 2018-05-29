import unittest
from django.test import TestCase
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from .models import TeacherData

class MyTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        TeacherData.objects.create(fname='John', lname='Boy')


    def test_first_name(self):
        teacher=TeacherData.objects.get(id=1)
        field_label = teacher._meta.get_field('fname').verbose_name
        self.assertEquals(field_label, 'fname')


if __name__ == '_main_':
    unittest.main()

