from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from loginPage import views
import requests
import time

def loginIndex (request):
    language = 'en-gb'
    sessions_language = 'en-gb'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    context = {}

    if request.method == 'POST':
        # uses django authentication module to check users
        user = auth.authenticate(username=request.POST.get('Username'), password=request.POST.get('Password'))
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('loggedIn'))

        else:
            return HttpResponseRedirect(reverse('invalid'))

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
