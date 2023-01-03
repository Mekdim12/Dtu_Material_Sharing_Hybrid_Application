from django.shortcuts import render,HttpResponse


def splashScreen(request):
    return render(request, 'index.html')

