import unittest
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'header.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Welcome to Pinelands Music School')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

    def test_career_url_by_name(self):
        response = self.client.get('/careers')
        self.assertEquals(response.status_code, 301)

    def test_about_url_by_name(self):
        response = self.client.get('/about')
        self.assertEquals(response.status_code, 301)

    def test_contact_url_by_name(self):
        response = self.client.get('/contact')
        self.assertEquals(response.status_code, 301)

    def test_browse_url_by_name(self):
        response = self.client.get('/browse')
        self.assertEquals(response.status_code, 301)

    def test_login_url_by_name(self):
        response = self.client.get('/login')
        self.assertEquals(response.status_code, 301)

    def test_account_url_by_name(self):
        response = self.client.get('/account/')
        self.assertEquals(response.status_code, 301)


if __name__ == '__main__':
    unittest.main()