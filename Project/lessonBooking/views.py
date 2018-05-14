from django.shortcuts import render

# Create your views here.
def browseClass(request):

    return render(request, 'lessonBooking/lessonBooking.html')

