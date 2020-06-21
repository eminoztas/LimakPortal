from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cv.models import Cv,Personnel
from home.models import PersonnelForm
from django import forms

# Create your views here.
def index(request):
    cv = Cv.objects.all()
    context = {'cv': cv} 
    return render(request, 'index.html', context)
    # return HttpResponse("You're looking at question %s." % text)


def AddPersonelCv(request):
    if request.method == 'POST':
            data = Cv()
            data.personnel=1
            data.title = request.POST.get('title')
            data.name = request.POST.get('name')
            data.surname = request.POST.get('surname')
            data.save()
            return HttpResponseRedirect('/')
    else :
        cv = Cv.objects.all()
        context = {'cv': cv} 
        return render(request, '/', context)
    

def AddPersonelCv2(request):
    if request.method == 'POST':
        form = PersonnelForm(request.POST,request.FILES)  
        if form.is_valid():
            data = Cv()
            data.title = form.cleaned_data['title']
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.save()
            return HttpResponseRedirect('/index')
    else :
        cv = Cv.objects.all()
        context = {'cv': cv} 
        return render(request, 'index.html', context)
    