from django.shortcuts import render, reverse
from .models import StudentData
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User


def student_account(request):
    if request.method == 'POST':
        FirstName = request.POST.get("FirstName")
        LastName = request.POST.get("LastName")
        UserName = request.POST.get("UserName")
        password = request.POST.get("password")
        Gender = request.POST.get("Gender")
        DoB = request.POST.get("DoB")
        HomeAddress = request.POST.get("HomeAddress")
        Email = request.POST.get("email")
        pNumber = request.POST.get("pNumber")
        preferredSubjects = request.POST.get("subjects")
        pFirstName = request.POST.get("pFirstName")
        pLastName = request.POST.get("pLastName")
        parentsNumber = request.POST.get("parentsNumber")
        pEmail = request.POST.get("pEmail")

        student_data = StudentData(FirstName=FirstName, LastName=LastName, Gender=Gender,
                                   UserName=UserName, password=password, DoB=DoB, HomeAddress=HomeAddress, Email=Email,
                                   pNumber=pNumber, preferredSubjects=preferredSubjects, pFirstName=pFirstName, pLastName=pLastName,
                                   parentsNumber = parentsNumber, pEmail = pEmail)
        student_data.save()
        user = User.objects.create_user(username=UserName, password=password, email=Email, first_name=FirstName,
                                        last_name=LastName)

        return HttpResponseRedirect(reverse('submitForm'))

    return render(request, 'student_account/student_account.html')

def submitForm(request):
    return render(request, 'contact_page/form_submitted.html')

