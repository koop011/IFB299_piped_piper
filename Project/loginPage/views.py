from django.shortcuts import render
import requests

# Create your views here.


def loginIndex (request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        print(username)
        print(password)


    return render(request, 'loginPage/loginHome.html', context)

