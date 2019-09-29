from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from first_app import forms


# Create your views here.

def index(request):
    webpg = AccessRecord.objects.order_by('date')
    DateDict = {'access_record': webpg}
    return render(request, "first_app/index.html", context=DateDict)


def staticTesting(request):
    myDict = {"placeholder": "Static Testing"}
    return render(request, "first_app/staticChecking.html", context=myDict)


def formView(request):
    form = forms.Form()

    if request.method == 'POST':
        form = forms.Form(request.POST)

        if form.is_valid():
            print("Valided")
            print("Name : " + form.cleaned_data['name'])
            print("Email : " + form.cleaned_data['email'])
            print("Text : " + form.cleaned_data['text'])

    return render(request, "first_app/formPage.html", context={'form': form})
