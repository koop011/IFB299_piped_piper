from django.shortcuts import render
from datetime import timedelta
from django.utils import timezone
from django.apps import apps
from .models import *
from collections import defaultdict


# Create your views here.
def browseClass(request):
    context = {}

    context['newStudent'] = newStudent(request)


    return render(request, 'lessonBooking/lessonBooking.html', context)


def timeBooking(request):
    context = {
        'timeSheet': {
            'electric_guitar_half_hour': {},
            'electric_guitar_hour': {},
            'keyboard_half_hour': {},
            'keyboard_hour': {},
            'piano_half_hour': {},
            'piano_hour': {},
            'guitar_half_hour': {},
            'guitar_hour': {},
            'drums_half_hour': {},
            'drums_hour': {},
            'violin_half_hour': {},
            'violin_hour': {},
            'saxophone_half_hour': {},
            'saxophone_hour': {},
            'flute_half_hour': {},
            'flute_hour': {},
            'cello_half_hour': {},
            'cello_hour': {},
            'clarinet_half_hour': {},
            'clarinet_hour': {},
        },
        'objects': {
            'electric_guitar_half_hour': electric_guitar_half_hour.objects.all(),
            'electric_guitar_hour': electric_guitar_hour.objects.all(),
            'keyboard_half_hour': keyboard_half_hour.objects.all(),
            'keyboard_hour': keyboard_hour.objects.all(),
            'piano_half_hour': piano_half_hour.objects.all(),
            'piano_hour': piano_hour.objects.all(),
            'guitar_half_hour': guitar_half_hour.objects.all(),
            'guitar_hour': guitar_hour.objects.all(),
            'drums_half_hour': drums_half_hour.objects.all(),
            'drums_hour': drums_hour.objects.all(),
            'violin_half_hour': violin_half_hour.objects.all(),
            'violin_hour': violin_hour.objects.all(),
            'saxophone_half_hour': saxophone_half_hour.objects.all(),
            'saxophone_hour': saxophone_hour.objects.all(),
            'flute_half_hour': flute_half_hour.objects.all(),
            'flute_hour': flute_hour.objects.all(),
            'cello_half_hour': cello_half_hour.objects.all(),
            'cello_hour': cello_hour.objects.all(),
            'clarinet_half_hour': clarinet_half_hour.objects.all(),
            'clarinet_hour': clarinet_hour.objects.all(),
        }
    }

    #counter = 0

    #print(context['objects']['electric_guitar_half_hour'])
    #print(keyboard_half_hour.objects.get(id=8).start_at)
    context['newStudent'] = newStudent(request)
    print(context['newStudent'])

    if request.method == "POST":
        context['instrument'] = request.POST.get('instruments')
        context['timePeriod'] = request.POST.get('timeChoice')
        context['timePeriod1'] = request.POST.get('timeChoice1')
        context['timePeriod2'] = request.POST.get('timeChoice2')
        context['timePeriod3'] = request.POST.get('timeChoice3')
        if context['newStudent']:
            print('new student')
            # timePeriod
            if context['timePeriod'] == 'half':
                context['instrument_time_half'] = context['instrument'] + '_' + context['timePeriod'] + '_' + 'hour'
                #half_class = context['instrument_time_half']
                if context['instrument_time_half'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_half']]:
                        context['timeSheet'][context['instrument_time_half']][i] = i.start_at
                        #defaultdict(context['instrument_time_half'])
                        print("List: ", context['timeSheet'][context['instrument_time_half']][i])

            if context['timePeriod'] == 'full':
                context['instrument_time_full'] = context['instrument'] + '_' + 'hour'
                #full_class = context['instrument_time_full']
                if context['instrument_time_full'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_full']]:
                        context['timeSheet'][context['instrument_time_full']][i] = i.start_at
                        #defaultdict(context['instrument_time_half'])
                        print("List: ", context['timeSheet'][context['instrument_time_full']][i])
        else:
            # timePeriod1
            if context['timePeriod1'] == 'half':
                context['instrument_time_half'] = context['instrument'] + '_' + context['timePeriod'] + '_' + 'hour'
                #half_class = context['instrument_time_half']
                if context['instrument_time_half'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_half']]:
                        context['timeSheet'][context['instrument_time_half']][i] = i.start_at
                        #defaultdict(context['instrument_time_half'])
                        print("List: ", context['timeSheet'][context['instrument_time_half']][i])

            else:
                context['instrument_time_full'] = context['instrument'] + '_' + 'hour'
                #full_class = context['instrument_time_full']
                if context['instrument_time_full'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_full']]:
                        context['timeSheet'][context['instrument_time_full']][i] = i.start_at
                        #defaultdict(context['instrument_time_half'])
                        print("List: ", context['timeSheet'][context['instrument_time_full']][i])

            # timePeriod2
            if context['timePeriod2'] == 'half':
                context['instrument_time_half'] = context['instrument'] + '_' + context['timePeriod'] + '_' + 'hour'
                #half_class = context['instrument_time_half']
                if context['instrument_time_half'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_half']]:
                        context['timeSheet'][context['instrument_time_half']][i] = i.start_at
                        #defaultdict(context['instrument_time_half'])
                        print("List: ", context['timeSheet'][context['instrument_time_half']][i])

            else:
                context['instrument_time_full'] = context['instrument'] + '_' + 'hour'
                #full_class = context['instrument_time_full']
                if context['instrument_time_full'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_full']]:
                        context['timeSheet'][context['instrument_time_full']][i] = i.start_at
                        #defaultdict(context['instrument_time_half'])
                        print("List: ", context['timeSheet'][context['instrument_time_full']][i])
            # timePeriod3
            if context['timePeriod3'] == 'half':
                context['instrument_time_half'] = context['instrument'] + '_' + context['timePeriod'] + '_' + 'hour'
                #half_class = context['instrument_time_half']
                if context['instrument_time_half'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_half']]:
                        context['timeSheet'][context['instrument_time_half']][i] = i.start_at
                        #defaultdict(context['instrument_time_half'])
                        print("List: ", context['timeSheet'][context['instrument_time_half']][i])

            else:
                context['instrument_time_full'] = context['instrument'] + '_' + 'hour'
                #full_class = context['instrument_time_full']
                if context['instrument_time_full'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_full']]:
                        context['timeSheet'][context['instrument_time_full']][i] = i.start_at
                        #defaultdict(context['instrument_time_half'])
                        print("List: ", context['timeSheet'][context['instrument_time_full']][i])







    return render(request, 'lessonBooking/timeBooking.html', context)


def lessonConfirm(request):
    studentModel = apps.get_model('student_account', 'StudentData')
    context = {}
    context['newStudent'] = newStudent(request)
    if request.method == "POST":

        # get student name
        currentstudent = studentModel.objects.filter(FirstName=request.user.first_name)
        print(studentModel.objects.all())
        first_name = request.user.first_name
        context['FirstName'] = first_name
        last_name = request.user.last_name
        context['LastName'] = last_name


        # get lesson time

        context['time'] = request.POST.get('instruments')
        print(context['time'])

        context['time1'] = request.POST.get('instruments1')
        print(context['time1'])

        context['time2'] = request.POST.get('instruments2')
        print(context['time2'])

        context['time3'] = request.POST.get('instruments3')
        print(context['time3'])




        # get instrument
        if request.POST.get('selected_instrument') == "cello":
            context['instrument'] = 'Cello'
        if request.POST.get('selected_instrument') == "clarinet":
            context['instrument'] = 'Clarinet'
        if request.POST.get('selected_instrument') == "drums":
            context['instrument'] = 'Drums'
        if request.POST.get('selected_instrument') == "electric_guitar":
            context['instrument'] = 'Electric Guitar'
        if request.POST.get('selected_instrument') == "flute":
            context['instrument'] = 'Flute'
        if request.POST.get('selected_instrument') == "guitar":
            context['instrument'] = 'Guitar'
        if request.POST.get('selected_instrument') == "keyboard":
            context['instrument'] = 'Keyboard'
        if request.POST.get('selected_instrument') == "piano":
            context['instrument'] = 'Piano'
        if request.POST.get('selected_instrument') == "saxophone":
            context['instrument'] = 'Saxophone'
        if request.POST.get('selected_instrument') == "violin":
            context['instrument'] = 'Violin'

        print(context['instrument'])
        # studentModel(instrument=context['instrument'])
        # print(studentModel.objects.all())
        #
        # pending_contract = pendingLessonContracts(first_name=first_name, last__name=last__name, instument=instrument, time=time)
        # pending_contract.save()





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

    N = 90

    date_N_days_ago = dtNow - timedelta(days=N)

    if dtJoined > date_N_days_ago:
        return True
    else:
        return False










