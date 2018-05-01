from django.shortcuts import render
#import templates

def index(request):
    return render(request, 'welcome_page/home.html')

def comingSoon(request):
    return render(request, 'comingSoon.html')


