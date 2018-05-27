from django.shortcuts import render


def ContactUsIndex(request):
    context = {}
    return render(request, 'Contact_us/ContactUs.html', context)

def comingSoon(request):
    context = {}
    return render(request, 'comingSoon.html', context)


