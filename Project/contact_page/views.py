from django.shortcuts import render


def index(request):
    return render(request, 'contact_page/contact.html')
