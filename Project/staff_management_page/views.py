from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404


def staff_managementIndex(request):
    context = {}
    return render(request, 'Staff_management_page/staff_management_page.html', context)

def comingSoon(request):
    context = {}
    return render(request, 'comingSoon.html', context)
#
# def adminRedirect(request):
#     return HttpResponseRedirect(request, 'http://localhost:8000/admin')
