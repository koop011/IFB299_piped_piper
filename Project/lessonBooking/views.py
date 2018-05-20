from django.shortcuts import render
#from Project.loginPage.models import Account

# Create your views here.
def browseClass(request):
    return render(request, 'lessonBooking/lessonBooking.html')

# def lessonConfirm(request):
#     context = {}
#     if request.method == "POST":
#         context['instrument'] = request.POST.get('instruments')
#         #Account(instruments=context['instrument'])
#
#         #check for the student status and assign time
#         if Account.objects.filter(student_status='new'):
#             #Account(instruments=context['instrument'])
#             pass
#         else:
#             #Account(instruments=context['instrument'])
#             pass
#         #Account.save()
#
#
#
#     return render(request, 'lessonBooking/lessonConfirm.html', context)



