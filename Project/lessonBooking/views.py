from django.shortcuts import render
from datetime import timedelta
from django.utils import timezone
from django.apps import apps
from .models import *
from collections import defaultdict


# Create your views here.
def browseClass(request):
    context = {
        'timeSheet':{
            'months': {},
        },
        'objects':{
            'months': period.objects.all(),
        }
    }
    context['newStudent'] = newStudent(request)
    for i in context['objects']['months']:
        context['timeSheet']['months'][i] = i.months

    return render(request, 'lessonBooking/lessonBooking.html', context)


def timeBooking(request):
    context = {
        'timeSheet': {
            'days': {},
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
            'days': days.objects.all(),
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
    context['contract_period'] = request.POST.get('months')
    for i in context['objects']['days']:
        context['timeSheet']['days'][i] = i.day


    if request.method == "POST":
        context['instrument'] = request.POST.get('instruments')
        context['timePeriod'] = request.POST.get('timeChoice')
        context['timePeriod1'] = request.POST.get('timeChoice1')
        context['timePeriod2'] = request.POST.get('timeChoice2')
        context['timePeriod3'] = request.POST.get('timeChoice3')

        # create dictionary of time schedule for each instruments
        if context['newStudent']:
            # timePeriod
            if context['timePeriod'] == 'half':
                context['instrument_time_half'] = context['instrument'] + '_' + context['timePeriod'] + '_' + 'hour'
                if context['instrument_time_half'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_half']]:
                        context['timeSheet'][context['instrument_time_half']][i] = i.start_at

            if context['timePeriod'] == 'full':
                context['instrument_time_full'] = context['instrument'] + '_' + 'hour'
                #full_class = context['instrument_time_full']
                if context['instrument_time_full'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_full']]:
                        context['timeSheet'][context['instrument_time_full']][i] = i.start_at
        else:
            # timePeriod1
            if context['timePeriod1'] == 'half':
                context['instrument_time_half'] = context['instrument'] + '_' + context['timePeriod'] + '_' + 'hour'
                #half_class = context['instrument_time_half']
                if context['instrument_time_half'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_half']]:
                        context['timeSheet'][context['instrument_time_half']][i] = i.start_at

            else:
                context['instrument_time_full'] = context['instrument'] + '_' + 'hour'
                #full_class = context['instrument_time_full']
                if context['instrument_time_full'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_full']]:
                        context['timeSheet'][context['instrument_time_full']][i] = i.start_at

            # timePeriod2
            if context['timePeriod2'] == 'half':
                context['instrument_time_half'] = context['instrument'] + '_' + context['timePeriod'] + '_' + 'hour'
                #half_class = context['instrument_time_half']
                if context['instrument_time_half'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_half']]:
                        context['timeSheet'][context['instrument_time_half']][i] = i.start_at

            else:
                context['instrument_time_full'] = context['instrument'] + '_' + 'hour'
                #full_class = context['instrument_time_full']
                if context['instrument_time_full'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_full']]:
                        context['timeSheet'][context['instrument_time_full']][i] = i.start_at
            # timePeriod3
            if context['timePeriod3'] == 'half':
                context['instrument_time_half'] = context['instrument'] + '_' + context['timePeriod'] + '_' + 'hour'
                #half_class = context['instrument_time_half']
                if context['instrument_time_half'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_half']]:
                        context['timeSheet'][context['instrument_time_half']][i] = i.start_at

            else:
                context['instrument_time_full'] = context['instrument'] + '_' + 'hour'
                #full_class = context['instrument_time_full']
                if context['instrument_time_full'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_full']]:
                        context['timeSheet'][context['instrument_time_full']][i] = i.start_at







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

        contract_period = request.POST.get('contract_period')
        print(contract_period)


        if context['newStudent']:
            # get lesson time
            time = '00:00:00'
            context['time'] = request.POST.get('instruments')
            time = context['time']
            print(context['time'])
        else:
            time1 = '00:00:00'
            context['time1'] = request.POST.get('instruments1')
            time1 = request.POST.get('instruments1')
            print(context['time1'])

            context['time2'] = request.POST.get('instruments2')
            print(context['time2'])
            time2 = request.POST.get('instruments2')

            context['time3'] = request.POST.get('instruments3')
            print(context['time3'])
            time3 = request.POST.get('instruments3')




        # get instrument
        instrument = 'none'
        if request.POST.get('selected_instrument') == "cello":
            context['instrument'] = 'Cello'
            instrument = context['instrument']
        if request.POST.get('selected_instrument') == "clarinet":
            context['instrument'] = 'Clarinet'
            instrument = context['instrument']
        if request.POST.get('selected_instrument') == "drums":
            context['instrument'] = 'Drums'
            instrument = context['instrument']
        if request.POST.get('selected_instrument') == "electric_guitar":
            context['instrument'] = 'Electric Guitar'
            instrument = context['instrument']
        if request.POST.get('selected_instrument') == "flute":
            context['instrument'] = 'Flute'
            instrument = context['instrument']
        if request.POST.get('selected_instrument') == "guitar":
            context['instrument'] = 'Guitar'
            instrument = context['instrument']
        if request.POST.get('selected_instrument') == "keyboard":
            context['instrument'] = 'Keyboard'
            instrument = context['instrument']
        if request.POST.get('selected_instrument') == "piano":
            context['instrument'] = 'Piano'
            instrument = context['instrument']
        if request.POST.get('selected_instrument') == "saxophone":
            context['instrument'] = 'Saxophone'
            instrument = context['instrument']
        if request.POST.get('selected_instrument') == "violin":
            context['instrument'] = 'Violin'
            instrument = context['instrument']

    return render(request, 'lessonBooking/lessonConfirm.html', context)



def bookingConfirm(request):
    context = {}
    context['newStudent'] = newStudent(request)
    if request.method == "POST":
        first_name = request.user.first_name
        context['FirstName'] = first_name
        last_name = request.user.last_name
        context['LastName'] = last_name
        print(first_name, last_name)

        instrument = request.POST.get('selected_instrument')
        print(instrument)
        contract_period = request.POST.get('contract_period')
        print(contract_period)

        # contract_period2 = context['contract_period']
        print(contract_period)
        context['instruments3'] = request.POST.get('time3')
        time3 = request.POST.get('time3')
        print(context['instruments3'])

        if context['newStudent']:
            # get lesson time
            time = '00:00:00'
            context['time'] = request.POST.get('instruments')
            time = context['time']
            print(context['time'])
        else:
            time1 = '00:00:00'
            context['time1'] = request.POST.get('time1')
            time1 = request.POST.get('time1')
            print(context['time1'])

            context['time2'] = request.POST.get('time2')
            print(context['time2'])
            time2 = request.POST.get('time2')

            context['time3'] = request.POST.get('instruments3')
            print(context['time3'])
            time3 = request.POST.get('instruments3')
            print(time3)




        if context['newStudent']:
            pending_contract_new = pendingLessonContracts_new(first_name=request.user.first_name, last_name=request.user.last_name,
                                                              instrument=instrument,
                                                              time=time)
            pending_contract_new.save()
        else:
            pending_contract_old = pendingLessonContracts_old(first_name=request.user.first_name, last_name=request.user.last_name,
                                                              instrument=instrument,
                                                              time1='working', time2='', time3=time3)
            pending_contract_old.save()

    return render(request, 'lessonBooking/bookingConfirm.html', context)


def newStudent(request):
    dtNow = timezone.now()
    dtJoined = request.user.date_joined

    N = 90

    date_N_days_ago = dtNow - timedelta(days=N)

    if dtJoined > date_N_days_ago:
        return True
    else:
        return False










