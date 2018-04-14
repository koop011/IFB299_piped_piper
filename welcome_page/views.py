from django.shortcuts import render

def index(request):
    return render(request, 'welcome_page/home.html')