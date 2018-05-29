from django.shortcuts import render


def AboutUsPageIndex(request):
    context = {}
    return render(request, 'about_us_page/about_us_page.html', context)




