import unittest
from django.test import TestCase

class test_login_page(TestCase):
    def setUp(self):
        self.expected_response_200 = 200
        self.expected_response_201 = 201
        self.expected_response_301 = 301
        self.expected_response_400 = 400

    def test_urls(self):
        response = self.client.get('/account/')
        self.assertEquals(response.status_code, self.expected_response_200)
        response = self.client.get('/account/Manage_Bookings')
        self.assertEquals(response.status_code, self.expected_response_301)
        response = self.client.get('/account/BookLesson')
        self.assertEquals(response.status_code, self.expected_response_301)
        response = self.client.get('/account/ManageContract')
        self.assertEquals(response.status_code, self.expected_response_301)
        response = self.client.get('/account/HireIntstrument')
        self.assertEquals(response.status_code, self.expected_response_301)
        response = self.client.get('/account/ConfirmContract')
        self.assertEquals(response.status_code, self.expected_response_301)
        response = self.client.get('/account/Feedback')
        self.assertEquals(response.status_code, self.expected_response_301)


if __name__ == '__main__':
    TestCase.main()
