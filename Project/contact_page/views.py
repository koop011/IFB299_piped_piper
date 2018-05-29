from django.shortcuts import render, reverse
from .models import TeacherData
from django.http import HttpResponse, HttpResponseRedirect, Http404





def submit_contact_form(request):
    context = {}
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        DoB = request.POST.get("DoB")
        HomeAddress = request.POST.get("HomeAddress")
        email = request.POST.get("email")
        pNumber = request.POST.get("pNumber")
        experience = request.POST.get("experience")
        certificates = request.POST.get("certificates")
        reference = request.POST.get("reference")
        # file = request.POST.get("file")
        if request.POST.get("electric_guitar") == 'on':
            electric_guitar = True
        else:
            electric_guitar = False
        if request.POST.get("guitar") == 'on':
            guitar = True
        else:
            guitar = False
        if request.POST.get("keyboard") == 'on':
            keyboard = True
        else:
            keyboard = False
        if request.POST.get("drums") == 'on':
            drums = True
        else:
            drums = False
        if request.POST.get("piano") == 'on':
            piano = True
        else:
            piano = False
        if request.POST.get("violin") == 'on':
            violin = True
        else:
            violin = False
        if request.POST.get("saxophone") == 'on':
            saxophone = True
        else:
            saxophone = False
        if request.POST.get("flute") == 'on':
            flute = True
        else:
            flute = False
        if request.POST.get("cello") == 'on':
            cello = True
        else:
            cello = False
        if request.POST.get("clarinet") == 'on':
            clarinet = True
        else:
            clarinet = False


        teacher_data = TeacherData(fname=fname, lname=lname, DoB=DoB, HomeAddress=HomeAddress, email=email, pNumber=pNumber,
                                   certificates=certificates, experience=experience, reference=reference, electric_guitar=electric_guitar,
                                   guitar=guitar, keyboard=keyboard, piano=piano, drums=drums, violin=violin, saxophone=saxophone,
                                   flute=flute, cello=cello, clarinet=clarinet)
        teacher_data.save()

        return HttpResponseRedirect(reverse('submitForm'))




    return render(request, 'contact_page/contact.html')

def submitForm(request):
    return render(request, 'contact_page/form_submitted.html')

def comingSoon(request):
    context = {}
    return render(request, 'comingSoon.html', context)

