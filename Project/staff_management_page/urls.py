from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_managementIndex, name='staff_managementIndex'),
    path('reportGeneration/', views.comingSoon, name='comingSoon'),
    path('admin/', views.comingSoon, name='comingSoon'),
    path('postEvent/', views.comingSoon, name='comingSoon'),
    path('contractApproval/', views.comingSoon, name='comingSoon'),
    path('StaffManagement/', views.comingSoon, name='comingSoon'),
]