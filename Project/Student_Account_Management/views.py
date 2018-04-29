from django.shortcuts import render


def StudentAccountIndex(request):
    context = {}
    return render(request, 'Student_Account_Management/Student_Account_Management.html', context)

def comingSoon(request):
    context = {}
    return render(request, 'comingSoon.html', context)

def bookLessons(request):
    return render(request, 'comingSoon.html')