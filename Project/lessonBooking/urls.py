from django.urls import path
from . import views

urlpatterns = [
    path('', views.browseClass, name='browseClass'),
    path('lessonConfirm/', views.lessonConfirm, name='lessonConfirm'),

]