from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.http import HttpResponseRedirect
from cv.models import Cv, Personnel
from home.models import CvForm
from django import forms
import requests
import json



# Create your views here.
def index(request):
    cv = Cv.objects.all()
    form = CvForm()
    context = {'cv': cv, 'form': form}
    "print(form)"
    return render(request, 'index.html', context)
    # return HttpResponse("You're looking at question %s." % text)


def AddPersonelCv(request):

    if request.method == 'POST':
        data = Cv()
        # import pdb; pdb.set_trace()
        print(data)
        data.personnel = Personnel.objects.get(id=1)
     
        data.ozet = request.POST.get('hakkımda')
        data.name = request.POST.get('name')
        data.surname = request.POST.get('surname')
        data.save()
        return HttpResponseRedirect('/')

    else :
        cv = Cv.objects.all()
        context = {'cv': cv}
        return render(request, '/', context)


def AddPersonelCv2(request):
    errors = {}

    if request.method == 'POST':
        form = CvForm(request.POST,request.FILES)
        import pdb; pdb.set_trace()
        if form.is_valid():
            instance = form.save(commit=False)
            instance.personnel = Personnel.objects.get(id=1)
            instance.save()

            return HttpResponseRedirect('/')
        else:
            errors = form.errors
    else:
        cv = Cv.objects.all()  
        form = CvForm(request.POST,request.FILES)

        context = {'cv': cv, 'form': form, 'errors': errors}
        return render(request, 'index.html', context)


def AddPersonelCv3(request):
    form = CvForm(request.POST)
    if form.is_valid():
        received_json_data = json.loads(json.dumps(form.cleaned_data))
        response = requests.post('https://limakcv.herokuapp.com/persons', json=received_json_data)
        if response.status_code != 201:
            import pdb; pdb.set_trace()
        else:
            print(response.text)
            return HttpResponseRedirect('/')
        # import pdb; pdb.set_trace()
    else:
        print(form.errors)

    return render(request, 'index.html', {})
