from django.shortcuts import render,HttpResponse


def splashScreen(request):
    print("----------------------------")
    return render(request, 'index.html')

def login(request):
    return render(request, 'LoginPage.html')