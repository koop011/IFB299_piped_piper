from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentAccountIndex, name='StudentAccountIndex'),
    path('Manage_Booking/', views.comingSoon, name='comingSoon'),
    path('BookLesson/', views.comingSoon, name='comingSoon'),
    # path('BookLesson/', views.comingSoon, name='comingSoon'),
    # path('BookLesson/', views.comingSoon, name='comingSoon'),
    # path('BookLesson/', views.comingSoon, name='comingSoon'),
    # path('BookLesson/', views.comingSoon, name='comingSoon'),




]