from django.shortcuts import render


# Create your views here.

def loginIndex (request):
    return render(request, 'loginPage/loginHome.html'  )