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
        GenderRadioOptions = request.POST.get("GenderRadioOptions")
        DoB = request.POST.get("DoB")
        HomeAddress = request.POST.get("HomeAddress")
        Email = request.POST.get("email")
        pNumber = request.POST.get("pNumber")
        subjects = request.POST.get("subjects")



        student_data = StudentData(FirstName=FirstName, LastName=LastName, GenderRadioOptions=GenderRadioOptions, UserName = UserName, password=password, DoB=DoB, HomeAddress=HomeAddress, Email=Email, pNumber=pNumber, subjects=subjects)
        student_data.save()
        user = User.objects.create_user(username=UserName, password=password, email=Email, first_name=FirstName, last_name=LastName)


        return HttpResponseRedirect(reverse('submitForm'))


    return render(request, 'student_account/student_account.html')

def submitForm(request):
    return render(request, 'contact_page/form_submitted.html')
