from django.urls import path
from . import views

urlpatterns = [
    path('', views.browseClass, name='browseClass'),
    path('lessonConfirm/', views.lessonConfirm, name='lessonConfirm'),
    path('timeBooking/', views.timeBooking, name='timeBooking'),
    path('bookingConfirm/', views.bookingConfirm, name='bookingConfirm'),

]