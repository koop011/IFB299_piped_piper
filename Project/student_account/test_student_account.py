import unittest
from django.test import TestCase
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from .models import StudentData
from django.apps import apps

class student_account_Tests(SimpleTestCase):

    def test_create_account_page_status_code(self):
        response = self.client.get('/create_account')
        self.assertEquals(response.status_code, 301)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('student_account'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_account/student_account.html')

    def test_create_page_contains_correct_html(self):
        response = self.client.get(reverse('student_account'))
        self.assertContains(response, 'Create a student account!')

    def test_create_page_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('student_account'))
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')


class StudentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        StudentData.objects.create(FirstName='Big', LastName='Bob', UserName='Bobby', password='password1', Gender='Male')

    def test_First_name_label(self):
        Student=StudentData.objects.get(id=1)
        field_label = Student._meta.get_field('FirstName').verbose_name
        self.assertEquals(field_label,'First Name')

    def test_Last_name_label(self):
        Student=StudentData.objects.get(id=1)
        field_label = Student._meta.get_field('LastName').verbose_name
        self.assertEquals(field_label,'LastName')

    def test_User_name_label(self):
        Student=StudentData.objects.get(id=1)
        field_label = Student._meta.get_field('UserName').verbose_name
        self.assertEquals(field_label,'UserName')

    def test_password_name_label(self):
        Student=StudentData.objects.get(id=1)
        field_label = Student._meta.get_field('password').verbose_name
        self.assertEquals(field_label,'password')

    def test_Gender_label(self):
        Student=StudentData.objects.get(id=1)
        field_label = Student._meta.get_field('Gender').verbose_name
        self.assertEquals(field_label,'Gender')

    def test_first_name_max_length(self):
        Student=StudentData.objects.get(id=1)
        max_length = Student._meta.get_field('FirstName').max_length
        self.assertEquals(max_length,200)

    def test_last_name_max_length(self):
        Student=StudentData.objects.get(id=1)
        max_length = Student._meta.get_field('LastName').max_length
        self.assertEquals(max_length,200)

    def test_user_name_max_length(self):
        Student=StudentData.objects.get(id=1)
        max_length = Student._meta.get_field('UserName').max_length
        self.assertEquals(max_length,20)

    def test_password_max_length(self):
        Student=StudentData.objects.get(id=1)
        max_length = Student._meta.get_field('password').max_length
        self.assertEquals(max_length,20)

    def test_Gender_max_length(self):
        Student=StudentData.objects.get(id=1)
        max_length = Student._meta.get_field('Gender').max_length
        self.assertEquals(max_length,7)

    def test_object_name_is_first_name(self):
        Student=StudentData.objects.get(id=1)
        expected_object_name = '%s' % (Student.FirstName)
        self.assertEquals(expected_object_name,str(Student))



if __name__ == '__main__':
    unittest.main()