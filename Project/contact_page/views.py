from django.shortcuts import render
from .models import TeacherData
from django.http import HttpResponse, HttpResponseRedirect, Http404


def submit_contact_form(request):
    if request.method == 'POST':
        FullName = request.POST.get("FullName")
        DoB = request.POST.get("DoB")
        HomeAddress = request.POST.get("HomeAddress")
        email = request.POST.get("email")
        pNumber = request.POST.get("DoB")
        certificates = request.POST.get("certificates")
        subjects = request.POST.get("subjects")

        teacher_data = TeacherData(FullName=FullName, DoB=DoB, HomeAddress=HomeAddress, email=email, pNumber=pNumber, certificates=certificates, subjects=subjects)
        teacher_data.save()

        return HttpResponse(submit_contact_form)


    return render(request, 'contact_page/contact.html')
