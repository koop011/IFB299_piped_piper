from django.shortcuts import render

# Create your views here.
def StudentAccountIndex(request):
    context = {}


    return render(request, 'Student_Account_Management/Student_Account_Management.html', context)