from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentAccountIndex, name='StudentAccountIndex'),
    path('Manage_Bookings/', views.comingSoon, name='comingSoon'),
    path('browse/', views.comingSoon, name='comingSoon'),
    path('ManageContract/', views.comingSoon, name='comingSoon'),
    path('HireIntstrument/', views.comingSoon, name='comingSoon'),
    path('ConfirmContract/', views.comingSoon, name='comingSoon'),
    path('Feedback/', views.comingSoon, name='comingSoon'),




]