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

    # def test_create_page_contains_correct_html(self):
    #     response = self.client.get('/create_account')
    #     self.assertContains(response, 'Create a student account!')

    # def test_create_page_does_not_contain_incorrect_html(self):
    #     response = self.client.get('/create_account')
    #     self.assertNotContains(
    #         response, 'Hi there! I should not be on the page.')


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        StudentData.objects.create(FirstName='Big', LastName='Bob')

    def test_first_name_label(self):
        author=StudentData.objects.get(id=1)
        field_label = author._meta.get_field('FirstName').verbose_name
        self.assertEquals(field_label,'FirstName')

    # def test_date_of_death_label(self):
    #     author=StudentData.objects.get(id=1)
    #     field_label = author._meta.get_field('date_of_death').verbose_name
    #     self.assertEquals(field_label,'died')

    def test_first_name_max_length(self):
        author=StudentData.objects.get(id=1)
        max_length = author._meta.get_field('FirstName').max_length
        self.assertEquals(max_length,200)

    # def test_object_name_is_last_name_comma_first_name(self):
    #     author=StudentData.objects.get(id=1)
    #     expected_object_name = '%s, %s' % (author.last_name, author.first_name)
    #     self.assertEquals(expected_object_name,str(author))

    # def test_get_absolute_url(self):
    #     author=StudentData.objects.get(id=1)
    #     #This will also fail if the urlconf is not defined.
    #     self.assertEquals(author.get_absolute_url(),'/catalog/author/1')


if __name__ == '__main__':
    unittest.main()