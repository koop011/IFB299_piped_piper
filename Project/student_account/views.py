from django.shortcuts import render, reverse
from .models import StudentData
from django.http import HttpResponse, HttpResponseRedirect, Http404


def student_account(request):
    if request.method == 'POST':
        FirstName = request.POST.get("FirstName")
        LastName = request.POST.get("LastName")
        password = request.POST.get("password")
        GenderRadioOptions = request.POST.get("GenderRadioOptions")
        DoB = request.POST.get("DoB")
        HomeAddress = request.POST.get("HomeAddress")
        Email = request.POST.get("email")
        pNumber = request.POST.get("DoB")
        subjects = request.POST.get("subjects")



        student_data = StudentData(FirstName=FirstName, LastName=LastName, password=password, GenderRadioOptions=GenderRadioOptions, DoB=DoB, HomeAddress=HomeAddress, Email=Email, pNumber=pNumber, subjects=subjects)
        student_data.save()

        # return HttpResponseRedirect(reverse('submitForm'))


    return render(request, 'student_account/student_account.html')
