from django.shortcuts import render
from .models import TeacherData


def index(request):
    return render(request, 'contact_page/contact.html')


def submit_contact_form(request):
    if request.method == 'POST':
        FullName = request.POST["FullName"]
        DoB = request.POST["DoB"]
        HomeAddress = request.POST["HomeAddress"]
        email = request.POST["email"]
        pNumber = request.POST["DoB"]
        certificates = request.POST["certificates"]
        subjects = request.POST["subjects"]

        teacher_data = TeacherData(FullName=FullName, DoB=DoB, HomeAddress=HomeAddress, email=email, pNumber=pNumber,
                                   certificates=certificates, subjects=subjects)
        teacher_data.save()
        print(FullName)
        print(DoB)
        print('form is donezo')
        all = TeacherData.objects.all()
        print('check:', all.objects.filter(FullName='test'))

    return render(request, 'contact_page/contact.html')
