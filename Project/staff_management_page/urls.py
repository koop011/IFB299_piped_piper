from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_managementIndex, name='staff_managementIndex'),
    path('reportGeneration/', views.comingSoon, name='comingSoon'),
    #path('editTheDatabase/', views.adminRedirect, name='adminRedirect'), # to admin page
    path('postEvent/', views.comingSoon, name='comingSoon'),
    path('contractApproval/', views.comingSoon, name='comingSoon'),
]