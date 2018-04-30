from django.shortcuts import render


def index(request):
    return render(request, 'student_account/student_account.html')