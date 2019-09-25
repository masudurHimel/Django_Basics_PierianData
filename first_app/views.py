from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    myDict = {"placeholder": "I am from index method"}
    return render(request, "first_app/index.html", context=myDict)

def staticTesting(request):
    myDict = {"placeholder": "Static Testing"}
    return render(request, "first_app/staticChecking.html", context=myDict)
