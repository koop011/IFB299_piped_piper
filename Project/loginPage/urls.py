from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginIndex, name='loginIndex'),
    path('loggedIn/', views.loggedIn, name='loggedIn'),
    path('loggedOut/', views.loggedOut, name='loggedOut'),
    path('invalid/', views.invalid, name='invalid'),
    path('retrieveAccount/', views.comingSoon)

]