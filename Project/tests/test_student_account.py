import unittest
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse


class student_account_Tests(SimpleTestCase):

    def test_create_account_page_status_code(self):
        response = self.client.get('/create_account')
        self.assertEquals(response.status_code, 301)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('student_account'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_account/student_account.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/create_account')
        self.assertContains(response, 'Create a student account!')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/create_account')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')


if __name__ == '__main__':
    unittest.main()