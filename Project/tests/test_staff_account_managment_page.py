import unittest
from django.test import TestCase


class MyTestCase(TestCase):
    def setUp(self):
        self.expected_response_200 = 200
        self.expected_response_201 = 201
        self.expected_response_301 = 301
        self.expected_response_400 = 400

    def test_urls(self):
        response = self.client.get('/staffManagement/')
        self.assertEquals(response.status_code, self.expected_response_200)
        response = self.client.get('/staffManagement/reportGeneration')
        self.assertEquals(response.status_code, self.expected_response_301)
        response = self.client.get('/staffManagement/admin')
        self.assertEquals(response.status_code, self.expected_response_301)
        response = self.client.get('/staffManagement/postEvent')
        self.assertEquals(response.status_code, self.expected_response_301)
        response = self.client.get('/staffManagement/contractApproval')
        self.assertEquals(response.status_code, self.expected_response_301)
        response = self.client.get('/staffManagement/StaffManagement')
        self.assertEquals(response.status_code, self.expected_response_301)

if __name__ == '__main__':
    TestCase.main()
