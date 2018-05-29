import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from .views import *
from django.test.client import RequestFactory

class test_login_page(TestCase):
    def setUp(self):
        self.expected_response_200 = 200
        self.expected_response_201 = 201
        self.expected_response_301 = 301
        self.expected_response_400 = 400
        self.factory = RequestFactory()
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()


    def test_urls_browse(self):
        login = self.client.login(username='testuser1', password='12345')
        response = self.client.get('/browse/')
        self.assertEquals(response.status_code, self.expected_response_200)

    def test_urls_browse(self):
        login = self.client.login(username='testuser1', password='12345')
        response = self.client.get('/browse/timeBooking')
        self.assertEquals(response.status_code, self.expected_response_301)

    def test_urls_timeBooking(self):
        login = self.client.login(username='testuser1', password='12345')
        response = self.client.get('/browse/lessonConfirm')
        self.assertEquals(response.status_code, self.expected_response_301)




    # def test_newUser(self):
    #     login = self.client.login(username='testuser1', password='12345')
    #     request = self.factory.get('/browse/timeBooking')
    #     response = timeBooking(request)
    #     expectedResult = True
    #
    #     result = newStudent(request)
    #
    #     self.assertEqual(result, expectedResult)

    # def test_oldUser(self):
    #     login = self.client.login(username='testuser1', password='12345')
    #     request = self.factory.get('/browse/timeBooking')
    #     response = timeBooking(request)
    #     expectedResult = False
    #
    #     result = newStudent(request)
    #
    #     self.assertEqual(result, expectedResult)



if __name__ == '__main__':
    TestCase.main()
