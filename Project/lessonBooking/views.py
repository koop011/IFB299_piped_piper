from django.shortcuts import render
from datetime import timedelta
from django.utils import timezone
from django.apps import apps
from .models import *
from datetime import datetime
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
            'electric_guitar_half_hour1': {},
            'electric_guitar_half_hour2': {},
            'electric_guitar_half_hour3': {},
            'electric_guitar_hour': {},
            'electric_guitar_hour1': {},
            'electric_guitar_hour2': {},
            'electric_guitar_hour3': {},
            'keyboard_half_hour': {},
            'keyboard_half_hour1': {},
            'keyboard_half_hour2': {},
            'keyboard_half_hour3': {},
            'keyboard_hour': {},
            'keyboard_hour1': {},
            'keyboard_hour2': {},
            'keyboard_hour3': {},
            'piano_half_hour': {},
            'piano_half_hour1': {},
            'piano_half_hour2': {},
            'piano_half_hour3': {},
            'piano_hour': {},
            'piano_hour1': {},
            'piano_hour2': {},
            'piano_hour3': {},
            'guitar_half_hour': {},
            'guitar_half_hour1': {},
            'guitar_half_hour2': {},
            'guitar_half_hour3': {},
            'guitar_hour': {},
            'guitar_hour1': {},
            'guitar_hour2': {},
            'guitar_hour3': {},
            'drums_half_hour': {},
            'drums_half_hour1': {},
            'drums_half_hour2': {},
            'drums_half_hour3': {},
            'drums_hour': {},
            'drums_hour1': {},
            'drums_hour2': {},
            'drums_hour3': {},
            'violin_half_hour': {},
            'violin_half_hour1': {},
            'violin_half_hour2': {},
            'violin_half_hour3': {},
            'violin_hour': {},
            'violin_hour1': {},
            'violin_hour2': {},
            'violin_hour3': {},
            'saxophone_half_hour': {},
            'saxophone_half_hour1': {},
            'saxophone_half_hour2': {},
            'saxophone_half_hour3': {},
            'saxophone_hour': {},
            'saxophone_hour1': {},
            'saxophone_hour2': {},
            'saxophone_hour3': {},
            'flute_half_hour': {},
            'flute_half_hour1': {},
            'flute_half_hour2': {},
            'flute_half_hour3': {},
            'flute_hour': {},
            'flute_hour1': {},
            'flute_hour2': {},
            'flute_hour3': {},
            'cello_half_hour': {},
            'cello_half_hour1': {},
            'cello_half_hour2': {},
            'cello_half_hour3': {},
            'cello_hour': {},
            'cello_hour1': {},
            'cello_hour2': {},
            'cello_hour3': {},
            'clarinet_half_hour': {},
            'clarinet_half_hour1': {},
            'clarinet_half_hour2': {},
            'clarinet_half_hour3': {},
            'clarinet_hour': {},
            'clarinet_hour1': {},
            'clarinet_hour2': {},
            'clarinet_hour3': {},
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



        # create dictionary of time schedule for each instruments
        if context['newStudent']:
            context['timePeriod'] = request.POST.get('timeChoice')
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
            context['timePeriod1'] = request.POST.get('timeChoice1')
            context['timePeriod2'] = request.POST.get('timeChoice2')
            context['timePeriod3'] = request.POST.get('timeChoice3')
            # timePeriod1
            if context['timePeriod1'] == 'half':
                context['instrument_time_half'] = context['instrument'] + '_' + context['timePeriod1'] + '_' + 'hour'
                #half_class = context['instrument_time_half']
                if context['instrument_time_half'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_half']]:
                        context['timeSheet'][context['instrument_time_half']+"1"][i] = i.start_at

            else:
                context['instrument_time_full'] = context['instrument'] + '_' + 'hour'
                #full_class = context['instrument_time_full']
                if context['instrument_time_full'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_full']]:
                        context['timeSheet'][context['instrument_time_full']+"1"][i] = i.start_at

            # timePeriod2
            if context['timePeriod2'] == 'half':
                context['instrument_time_half'] = context['instrument'] + '_' + context['timePeriod2'] + '_' + 'hour'
                #half_class = context['instrument_time_half']
                if context['instrument_time_half'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_half']]:
                        context['timeSheet'][context['instrument_time_half']+"2"][i] = i.start_at
            else:
                context['instrument_time_full'] = context['instrument'] + '_' + 'hour'
                #full_class = context['instrument_time_full']
                if context['instrument_time_full'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_full']]:
                        context['timeSheet'][context['instrument_time_full']+"2"][i] = i.start_at
            # timePeriod3
            if context['timePeriod3'] == 'half':
                context['instrument_time_half'] = context['instrument'] + '_' + context['timePeriod3'] + '_' + 'hour'
                #half_class = context['instrument_time_half']
                if context['instrument_time_half'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_half']]:
                        context['timeSheet'][context['instrument_time_half']+"3"][i] = i.start_at

            else:
                context['instrument_time_full'] = context['instrument'] + '_' + 'hour'
                #full_class = context['instrument_time_full']
                if context['instrument_time_full'] in context['timeSheet']:
                    for i in context['objects'][context['instrument_time_full']]:
                        context['timeSheet'][context['instrument_time_full']+"3"][i] = i.start_at







    return render(request, 'lessonBooking/timeBooking.html', context)


def lessonConfirm(request):
    studentModel = apps.get_model('student_account', 'StudentData')
    context = {}
    context['newStudent'] = newStudent(request)

    if request.method == "POST":
        if context['newStudent']:
            context['day'] = request.POST.get('days')
            context['timePeriod'] = request.POST.get('timePeriod')
        else:
            context['day1'] = request.POST.get('days1')
            context['day2'] = request.POST.get('days2')
            context['day3'] = request.POST.get('days3')
            context['timePeriod1'] = request.POST.get('timePeriod1')
            context['timePeriod2'] = request.POST.get('timePeriod2')
            context['timePeriod3'] = request.POST.get('timePeriod3')
            print("timePeriod1: ", context['timePeriod1']) # half, full
            print("timePeriod2: ", context['timePeriod2']) # half, full
            print("timePeriod3: ", context['timePeriod3']) # half, full

        # get student name
        #currentstudent = studentModel.objects.filter(FirstName=request.user.first_name)
        #print(studentModel.objects.all())
        first_name = request.user.first_name
        context['FirstName'] = first_name
        last_name = request.user.last_name
        context['LastName'] = last_name

        #contract_period = request.POST.get('contract_period')
        #print(contract_period)
        context['contract_period'] = request.POST.get('contract_period')



        context['selected_instrument'] = request.POST.get('selected_instrument')
        context['instrument'] = request.POST.get('selected_instrument')
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

        if context['newStudent']:
            # get lesson time

            context['time'] = request.POST.get('instruments')
            d = datetime.strptime(context['time'], "%H:%M:%S")
            t = d.time()
            ft = t.strftime("%I:%M %p")
            print(ft)
            context['ft'] = ft
            print(context['time'])
            time = context['time']
            print("new student  Time : ", context['time'])

        else:

            context['time1'] = request.POST.get('instruments1')
            d1 = datetime.strptime(context['time1'], "%H:%M:%S")
            t1 = d1.time()
            ft1 = t1.strftime("%I:%M %p")
            print(ft1)
            context['ft1'] = ft1
            print(context['time1'])

            context['time2'] = request.POST.get('instruments2')
            d2 = datetime.strptime(context['time2'], "%H:%M:%S")
            t2 = d2.time()
            ft2 = t2.strftime("%I:%M %p")
            print(ft2)
            context['ft2'] = ft2
            print(context['time2'])

            context['time3'] = request.POST.get('instruments3')
            d3 = datetime.strptime(context['time3'], "%H:%M:%S")
            t3 = d3.time()
            ft3 = t3.strftime("%I:%M %p")
            print(ft3)
            context['ft3'] = ft3
            print(context['time3'])





            # get instrument




        return render(request, 'lessonBooking/lessonConfirm.html', context)



def bookingConfirm(request):
    context = {}
    context['newStudent'] = newStudent(request)

    if request.method == "POST":
        context['selected_instrument'] = request.POST.get('selected_instrument')
        context['contract_period'] = request.POST.get('contract_period')
        context['timePeriod']= request.POST.get('timePeriod')
        print("Instrument: ", context['selected_instrument'])
        print("Contract Period: ", context['contract_period'])

        if context['newStudent']:
            context['time'] = request.POST.get('time')
            context['day'] = request.POST.get('day')
            context['timePeriod'] = request.POST.get('timePeriod')
            print("Time: ", context['time'])
            print("DAY: ", context['day'])
            print("timePeriod: ", context['timePeriod']) # half, full
        else:
            context['time1'] = request.POST.get('time1')


            context['time2'] = request.POST.get('time2')
            # d1 = datetime.strptime(request.POST.get('time1'), "%H:%M:%S")
            # t1 = d1.time()
            # ft1 = t1.strftime("%H:%M %p")
            # print(ft1)

            context['time3'] = request.POST.get('time3')
            # d1 = datetime.strptime(request.POST.get('time1'), "%H:%M:%S")
            # t1 = d1.time()
            # ft1 = t1.strftime("%H:%M %p")
            # print(ft1)

            context['day1'] = request.POST.get('day1')
            context['day2'] = request.POST.get('day2')
            context['day3'] = request.POST.get('day3')
            context['timePeriod1'] = request.POST.get('timePeriod1')
            context['timePeriod2'] = request.POST.get('timePeriod2')
            context['timePeriod3'] = request.POST.get('timePeriod3')
            print("Time1: ", context['time1'])
            print("Time2: ", context['time2'])
            print("Time3: ", context['time3'])
            print("DAY1: ", context['day1'])
            print("DAY2: ", context['day2'])
            print("DAY3: ", context['day3'])
            print("timePeriod1: ", context['timePeriod1']) # half, full
            print("timePeriod2: ", context['timePeriod2']) # half, full
            print("timePeriod3: ", context['timePeriod3']) # half, full


        if context['newStudent']:
            pending_contract_new = pendingLessonContracts_new(first_name=request.user.first_name, last_name=request.user.last_name,
                                                              contract_period=request.POST.get('contract_period'),
                                                              instrument=request.POST.get('selected_instrument'),
                                                              time=request.POST.get('time'),
                                                              day=request.POST.get('day'),
                                                              timePeriod=request.POST.get('timePeriod'))
            pending_contract_new.save()
        else:
            pending_contract_old = pendingLessonContracts_old(first_name=request.user.first_name, last_name=request.user.last_name,
                                                              contract_period=request.POST.get('contract_period'),
                                                              instrument=request.POST.get('selected_instrument'),
                                                              time1=request.POST.get('time1'), time2=request.POST.get('time2'), time3=request.POST.get('time3'),
                                                              day1=request.POST.get('day1'), day2=request.POST.get('day2'), day3=request.POST.get('day3'),
                                                              timePeriod1=request.POST.get('timePeriod1'), timePeriod2=request.POST.get('timePeriod2'), timePeriod3=request.POST.get('timePeriod3'))
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










