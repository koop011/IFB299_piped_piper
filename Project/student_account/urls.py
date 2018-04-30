from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_account, name='student_account'),
]
