from django.shortcuts import render,HttpResponse

# Create your views here.

def adminSplashScreen(request):
    return HttpResponse("i am from doh page")