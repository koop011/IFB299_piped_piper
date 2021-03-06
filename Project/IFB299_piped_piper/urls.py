"""IFB299_piped_piper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('welcome_page.urls')),
    path('careers/', include('contact_page.urls')),
    path('account/', include('Student_Account_Management.urls')),
    path('contact/', include('welcome_page.urls')),
    path('login/', include('loginPage.urls')),
    path('create_account/', include('student_account.urls')),
    path('student/', include('loginPage.urls')),
    path('staffManagement/', include('staff_management_page.urls')),
    path('login/', include('loginPage.urls'), name='login'),
    path('aboutus/',include('about_us_page.urls')),
    path('browse/', include('lessonBooking.urls'), name='lessonBooking'),
    path('contactus/', include('Contact_Us.urls')),
]
