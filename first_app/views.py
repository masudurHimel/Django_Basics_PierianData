from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord


# Create your views here.

def index(request):
    webpg = AccessRecord.objects.order_by('date')
    DateDict = {'access_record': webpg}
    return render(request, "first_app/index.html", context=DateDict)


def staticTesting(request):
    myDict = {"placeholder": "Static Testing"}
    return render(request, "first_app/staticChecking.html", context=myDict)
