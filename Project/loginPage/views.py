from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate
import requests


def loginIndex (request):
    context = {}

    if request.method == 'POST':
        # uses django authentication module to check users
        user = authenticate(username=request.POST.get('Username'), password=request.POST.get('Password'))

        if user is not None:
            return HttpResponse("Passed")
            # redirect(reverse('index'))

        else:
            return HttpResponse("Failed")

    return render(request, 'loginPage/loginHome.html', context)

