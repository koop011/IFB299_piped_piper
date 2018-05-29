from importlib import import_module

from django.core.handlers.wsgi import WSGIRequest

from .views import *
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse, resolve
import base64
# from mock import MagicMock, patch
from requests import Response

'''
Unit tests are limited as the functions used within the loginPage.views uses a Django module which needs sessions.
Sessions are necessary to use the authentication function which cannot be accessed through testing.
The loginPage uses this authentication to function to redirect various users to different htmls and states.
'''
class test_login_page(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.expected_response_200 = 200
        self.expected_response_201 = 201
        self.expected_response_301 = 301
        self.expected_response_400 = 400

        self.user = User.objects.create_user('test', None, 'testing')
        self.user.save()

    def test_login_url(self):
        path = reverse('loginIndex')
        assert resolve(path).view_name == 'loginIndex'
        response = self.client.get('/login/')
        self.assertEquals(response.status_code, self.expected_response_200)

    def test_urls(self):
        response = self.client.get('/login/loggedOut')
        self.assertEquals(response.status_code, self.expected_response_301)

    def test_urls(self):
        response = self.client.get('/login/loggedIn')
        self.assertEquals(response.status_code, self.expected_response_301)

    def test_urls(self):
        response = self.client.get('/login/invalid')
        self.assertEquals(response.status_code, self.expected_response_301)

    def test_user_invalid(self):

        #self.client.login(username='tester', password='testing')
        request = self.factory.post('/login', data={'Username':'tester', 'Password':'testing'})
        response = loginIndex(request)
        self.assertTrue(response)


'''
Code graveyard for session unit testing and authentication
'''
        # request = self.factory.get('/login/loggedOut')
        # request.user = self.user
        # response = loggedOut(request)
        # self.assertEquals(response.status_code, self.expected_response_200)

    # def test_authentication(self):
    #     s = self.client.session
    #     s.update({
    #         "expire_date": '2018-12-05',
    #         "session_key": '-z8$$1g6uo(gp2kq0t)fv$#)^r9$d@80spq(+9wlo*68tfk6di',
    #     })
    #     s.save()
    #     response = self.client.post('/login', data={'Username':'test', 'Password':'testing'})
    #     self.assertEqual(response.status_code, 301)
        # c = Client()
        # request = self.factory.post('/login', data={'Username':'test', 'Password':'testing'})
        # response = loginIndex(request)
        # #response = c.post('/login', data={'Username':'test', 'Password':'testing'})
        # #response = loginIndex(request)
        #
        # self.assertEqual(response.status_code, 200)

        # session = self.client.session
        # session['-z8$$1g6uo(gp2kq0t)fv$#)^r9$d@80spq(+9wlo*68tfk6di'] = 'test'
        # session.save()
        # c = Client()
        # request = self.factory.post('/login', data={'Username':'test', 'Password':'testing'})
        # response = loginIndex(request)
        # #response = c.post('/login', data={'Username':'test', 'Password':'testing'})
        # #response = loginIndex(request)
        #
        # self.assertEqual(response.status_code, 200)
    #
    #

    #
    # def test_user_log_out(self):
    #     self.client.login(username='testUser', password='testing')
    #     request = self.factory.get(reverse('loggedOut'))
    #     response = loggedOut(request)
    #     self.assertTrue(response)


    # def test_logout(self):
    #     # Log in
    #     self.client.login(username='XXX', password="XXX")
    #
    #     # Check response code
    #     response = self.client.get('/login')
    #     self.assertEquals(response.status_code, 200)
    #
    #     # Check 'Log out' in response
    #     self.assertTrue('Log out' in response.content)
    #
    #     # Log out
    #     self.client.logout()
    #
    #     # Check response code
    #     response = self.client.get('/admin/login')
    #     self.assertEquals(response.status_code, 200)
    #
    #     # # Check 'Log in' in response
    #     # self.assertTrue('Log in' in response.content)
    #
    #






    #def
    #
    # @patch('IFB299_git.Project.loginPage.views.requests.post')
    # def test_log_in_out(self, mock_post):
    #     mock_reponse = MagicMock(spec=Response)
    #     mock_reponse.status_code = self.expected_reponse_200
    #
    #     mock_post.return_value = mock_reponse
    #
    #     response = self.client.post(username='testUser',password='testing')



    # def test_loginPage_status_code(self):
    #     response = self.client.get('/login')
    #     self.assertEquals(response.status_code, 200)
#
#     def test_view_url_by_name(self):
#         response = self.client.get(reverse('home'))
#         self.assertEquals(response.status_code, 200)
#
#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('home'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'header.html')
#
#     def test_home_page_contains_correct_html(self):
#         response = self.client.get('/')
#         self.assertContains(response, 'Welcome to Pinelands Music School')
#
#     def test_home_page_does_not_contain_incorrect_html(self):
#         response = self.client.get('/')
#         self.assertNotContains(
#             response, 'Hi there! I should not be on the page.')
#
#
#

if __name__ == '__main__':
    TestCase.main()
