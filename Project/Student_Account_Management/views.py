from django.shortcuts import render


def StudentAccountIndex(request):
    context = {}
    return render(request, 'Student_Account_Management/Student_Account_Management.html', context)

def comingSoon(request):
    context = {}
    return render(request, 'Manage_Booking/comingSoon.html', context)

def bookLessons(request):
    return render(request, 'BookLesson/comingSoon.html')

def bookLessons(request):
    return render(request, 'ManageContract/comingSoon.html')

def bookLessons(request):
    return render(request, 'HireIntstrument/comingSoon.html')

def bookLessons(request):
    return render(request, 'ConfirmContract/comingSoon.html')

def bookLessons(request):
    return render(request, 'Feedback/comingSoon.html')

