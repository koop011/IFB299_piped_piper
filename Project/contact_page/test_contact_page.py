import unittest
from django.test import TestCase
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from .models import TeacherData

# class MyTestCase(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         #Set up non-modified objects used by all test methods
#         TeacherData.objects.create(fname='John', lname='Boy')
#
#
#     def test_first_name(self):
#         teacher=TeacherData.objects.get(id=1)
#         field_label = teacher._meta.get_field('fname').verbose_name
#         self.assertEquals(field_label, 'fname')

class TeacherModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        TeacherData.objects.create(fname='Small', lname='Bob')

    def test_First_name_label(self):
        Teacher=TeacherData.objects.get(id=1)
        field_label = Teacher._meta.get_field('fname').verbose_name
        self.assertEquals(field_label,'fname')

    def test_Last_name_label(self):
        Teacher=TeacherData.objects.get(id=1)
        field_label = Teacher._meta.get_field('lname').verbose_name
        self.assertEquals(field_label,'lname')

    def test_User_name_label(self):
        Teacher=TeacherData.objects.get(id=1)
        field_label = Teacher._meta.get_field('DoB').verbose_name
        self.assertEquals(field_label,'DoB')

    def test_password_name_label(self):
        Teacher=TeacherData.objects.get(id=1)
        field_label = Teacher._meta.get_field('HomeAddress').verbose_name
        self.assertEquals(field_label,'HomeAddress')

    def test_Gender_label(self):
        Teacher=TeacherData.objects.get(id=1)
        field_label = Teacher._meta.get_field('email').verbose_name
        self.assertEquals(field_label,'email')

    def test_Number_label(self):
        Teacher=TeacherData.objects.get(id=1)
        field_label = Teacher._meta.get_field('pNumber').verbose_name
        self.assertEquals(field_label,'pNumber')

    def test_Certificate_label(self):
        Teacher=TeacherData.objects.get(id=1)
        field_label = Teacher._meta.get_field('certificates').verbose_name
        self.assertEquals(field_label,'certificates')

    def test_Experience_label(self):
        Teacher=TeacherData.objects.get(id=1)
        field_label = Teacher._meta.get_field('experience').verbose_name
        self.assertEquals(field_label,'experience')

    def test_Reference_label(self):
        Teacher=TeacherData.objects.get(id=1)
        field_label = Teacher._meta.get_field('reference').verbose_name
        self.assertEquals(field_label,'reference')

    def test_fname_max_length(self):
        Teacher=TeacherData.objects.get(id=1)
        max_length = Teacher._meta.get_field('fname').max_length
        self.assertEquals(max_length,200)

    def test_lname_max_length(self):
        Teacher=TeacherData.objects.get(id=1)
        max_length = Teacher._meta.get_field('lname').max_length
        self.assertEquals(max_length,200)

    def test_DoB_max_length(self):
        Teacher=TeacherData.objects.get(id=1)
        max_length = Teacher._meta.get_field('DoB').max_length
        self.assertEquals(max_length,20)

    def test_HomeAddress_max_length(self):
        Teacher=TeacherData.objects.get(id=1)
        max_length = Teacher._meta.get_field('HomeAddress').max_length
        self.assertEquals(max_length,200)

    def test_email_max_length(self):
        Teacher=TeacherData.objects.get(id=1)
        max_length = Teacher._meta.get_field('email').max_length
        self.assertEquals(max_length,200)

    def test_pNumber_max_length(self):
        Teacher=TeacherData.objects.get(id=1)
        max_length = Teacher._meta.get_field('pNumber').max_length
        self.assertEquals(max_length,13)

    def test_certificates_max_length(self):
        Teacher=TeacherData.objects.get(id=1)
        max_length = Teacher._meta.get_field('certificates').max_length
        self.assertEquals(max_length,200)

    def test_experience_max_length(self):
        Teacher=TeacherData.objects.get(id=1)
        max_length = Teacher._meta.get_field('experience').max_length
        self.assertEquals(max_length,200)

    def test_reference_max_length(self):
        Teacher=TeacherData.objects.get(id=1)
        max_length = Teacher._meta.get_field('reference').max_length
        self.assertEquals(max_length,200)

    # def test_Electric_Guitar_label(self):
    #     Teacher=TeacherData.objects.get(id=1)
    #     field_label = Teacher._meta.get_field('electric_guitar').verbose_name
    #     self.assertEquals(field_label,'electric_guitar')
    #
    # def test_Guitar_label(self):
    #     Teacher=TeacherData.objects.get(id=1)
    #     field_label = Teacher._meta.get_field('guitar').verbose_name
    #     self.assertEquals(field_label,'guitar')
    #
    # def test_Keyboard_label(self):
    #     Teacher=TeacherData.objects.get(id=1)
    #     field_label = Teacher._meta.get_field('keyboard').verbose_name
    #     self.assertEquals(field_label,'keyboard')
    #
    # def test_Piano_label(self):
    #     Teacher=TeacherData.objects.get(id=1)
    #     field_label = Teacher._meta.get_field('piano').verbose_name
    #     self.assertEquals(field_label,'piano')
    #
    # def test_Drums_label(self):
    #     Teacher=TeacherData.objects.get(id=1)
    #     field_label = Teacher._meta.get_field('drums').verbose_name
    #     self.assertEquals(field_label,'drums')
    #
    # def test_Violin_label(self):
    #     Teacher=TeacherData.objects.get(id=1)
    #     field_label = Teacher._meta.get_field('violin').verbose_name
    #     self.assertEquals(field_label,'violin')
    #
    # def test_Saxophone_label(self):
    #     Teacher=TeacherData.objects.get(id=1)
    #     field_label = Teacher._meta.get_field('saxophone').verbose_name
    #     self.assertEquals(field_label,'saxophone')
    #
    # def test_Flute_label(self):
    #     Teacher=TeacherData.objects.get(id=1)
    #     field_label = Teacher._meta.get_field('flute').verbose_name
    #     self.assertEquals(field_label,'flute')
    #
    # def test_Cello_label(self):
    #     Teacher=TeacherData.objects.get(id=1)
    #     field_label = Teacher._meta.get_field('cello').verbose_name
    #     self.assertEquals(field_label,'cello')
    #
    # def test_Clarinet_label(self):
    #     Teacher=TeacherData.objects.get(id=1)
    #     field_label = Teacher._meta.get_field('clarinet').verbose_name
    #     self.assertEquals(field_label,'clarinet')



    def test_object_name_is_first_name(self):
        Teacher=TeacherData.objects.get(id=1)
        expected_object_name = '%s %s' % (Teacher.fname, Teacher.lname)
        self.assertEquals(expected_object_name,str(Teacher))


if __name__ == '_main_':
    unittest.main()

