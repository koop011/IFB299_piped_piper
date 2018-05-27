from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, reverse
from django.contrib import auth


def loginIndex (request):
    context = {}

    if request.method == 'POST':
        print('CHECK: ', request.POST.get('Username'), " ", request.POST.get('Password'))
        # uses django authentication module to check users
        user = auth.authenticate(username=request.POST.get('Username'), password=request.POST.get('Password'))
        if user is not None:
            # if user.is_staff:
            #     return HttpResponseRedirect('/admin')

            auth.login(request, user)
            return HttpResponseRedirect(reverse('loggedIn'))

        else:
            return HttpResponseRedirect(reverse('invalid'))
    #raise Http404
    return render(request, 'loginPage/loginHome.html', context, )


def loggedIn(request):
    context = {}
    return render(request, 'loginPage/loggedIn.html', context)


def loggedOut(request):
    context={}
    auth.logout(request)
    return render(request, 'loginPage/loggedOut.html', context)


def invalid(request):
    context={}
    return render(request, 'loginPage/invalid.html', context)

def retrieveAccount(request):
    return render(request, 'loginPage/retrieve.html')

def comingSoon(request):
    context = {}
    return render(request, 'comingSoon.html', context)