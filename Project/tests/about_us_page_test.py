import unittest
from django.test import TestCase


class MyTestCase(TestCase):
    def setUp(self):
        self.expected_response_200 = 200
        self.expected_response_201 = 201
        self.expected_response_301 = 301
        self.expected_response_400 = 400

    def test_urls(self):
        response = self.client.get('/aboutus/')
        self.assertEquals(response.status_code, self.expected_response_200)

if __name__ == '__main__':
    TestCase.main()
