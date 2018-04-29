# Have a function which takes in input from the user of the variables, Full name, Date of Birth, Home address,
# Email, Phone number, Qualifications, Certificates and subjects they wish to teach

from django.test import TestCase
from django.test import Client
from .forms import *   # import all forms




class Setup_Class(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="user@mp.com", password="user", first_name="user", phone=12345678)

class User_Form_Test(TestCase):

    # Valid Form Data
    def test_UserForm_valid(self):
        form = UserForm(data={'email': "user@mp.com", 'password': "user", 'first_name': "user", 'phone': 12345678})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = UserForm(data={'email': "", 'password': "mp", 'first_name': "mp", 'phone': ""})
        self.assertFalse(form.is_valid())

class Views_Form_Test(SetUp_Class):

    def test_home_view(self):
        user_login = self.client.login(email="user@mp.com", password="user")
        self.assertTrue(user_login)
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)

    def test_add_user_view(self):
        response = self.client.get("include url for add user view")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "include template name to render the response")

    # Invalid Data
    def test_add_user_invalidform_view(self):
        response = self.client.post("include url to post the data given", {'email': "admin@mp.com", 'password': "", 'first_name': "mp", 'phone': 12345678})
        self.assertTrue('"error": true' in response.content)

    # Valid Data
    def test_add_admin_form_view(self):
        user_count = User.objects.count()
        response = self.client.post("include url to post the data given", {'email': "user@mp.com", 'password': "user", 'first_name': "user"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), user_count+1)
        self.assertTrue('"error": false' in response.content)



if __name__ == '__main__':
    TestCase.main()