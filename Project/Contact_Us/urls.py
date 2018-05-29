from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUsIndex, name='ContactUsIndex'),
    path('profile/', views.comingSoon, name='comingSoon'),





]