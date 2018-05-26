from django.shortcuts import render
from datetime import timedelta
from django.utils import timezone
from django.apps import apps

# Create your views here.


def browseClass(request):
    context = {}

    context['newStudent'] = newStudent(request)
    print(context['newStudent'])


    return render(request, 'lessonBooking/lessonBooking.html', context)

def lessonConfirm(request):

    studentModel = apps.get_model('student_account', 'StudentData')
    context = {}
    if request.method == "POST":
        context['instrument'] = request.POST.get('instruments')
        studentModel(instrument=context['instrument'])
        print(studentModel.objects.all())

        # currentStudent = studentModel.objects.filter(username=request.user.username)
        # first_name = currentStudent.first_name
        # context['firstname'] = first_name

        # context = {
        #   'firstname': first_name,
        #   'lastname': last_name,
        # }
        # currentSTudnet.


        #
        # #check for the student status and assign time
        # if StudentData.objects.filter(student_status='new'):
        #     #Account(instruments=context['instrument'])
        #     pass
        # else:
        #     #Account(instruments=context['instrument'])
        #     pass
        # #Account.save()


    return render(request, 'lessonBooking/lessonConfirm.html', context)


def newStudent(request):
    dtNow = timezone.now()
    dtJoined = request.user.date_joined
    new = 'new'
    old = 'old'

    N = 90

    date_N_days_ago = dtNow - timedelta(days=N)
    
    if dtJoined > date_N_days_ago:
        return True
    else:
        return False










