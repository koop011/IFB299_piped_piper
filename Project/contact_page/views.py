from django.shortcuts import render, reverse
from .models import TeacherData
from django.http import HttpResponse, HttpResponseRedirect, Http404


def submit_contact_form(request):
    context = {}
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        DoB = request.POST.get("DoB")
        HomeAddress = request.POST.get("HomeAddress")
        email = request.POST.get("email")
        pNumber = request.POST.get("DoB")
        certificates = request.POST.get("certificates")
        subjects = request.POST.get("subjects")
        file = request.POST.get("file")

        teacher_data = TeacherData(fname=fname, lname=lname, DoB=DoB, HomeAddress=HomeAddress, email=email, pNumber=pNumber, certificates=certificates, subjects=subjects, file=file)
        teacher_data.save()

        return HttpResponseRedirect(reverse('submitForm'))


    return render(request, 'contact_page/contact.html')

def submitForm(request):
    return render(request, 'contact_page/form_submitted.html')

def comingSoon(request):
    context = {}
    return render(request, 'comingSoon.html', context)