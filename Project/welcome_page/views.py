from django.shortcuts import render
import templates

def index(request):
    return render(request, 'templates.welcome_page.home.html')