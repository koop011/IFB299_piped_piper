from django.shortcuts import render



def staff_managementIndex(request):
    context = {}
    return render(request, 'Staff_management_page/staff_management_page.html', context)

