from django.shortcuts import render



def staff_managementIndex(request):
    context = {}
    return render(request, 'Staff_management_page/staff_management_page.html', context)

def comingSoon(request):
    context = {}
    return render(request, 'reportGeneration/comingSoon.html', context)

def comingSoon(request):
    context = {}
    return render(request, 'editTheDatabase/comingSoon.html', context)

def comingSoon(request):
    context = {}
    return render(request, 'postEvent/comingSoon.html', context)

def comingSoon(request):
    context = {}
    return render(request, 'contractApproval/comingSoon.html', context)

def comingSoon(request):
    context = {}
    return render(request, 'StaffManagement/comingSoon.html', context)