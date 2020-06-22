from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from cv.models import Cv, Personnel
from home.models import PersonnelForm
from django import forms

# Create your views here.
def index(request):
    cv = Cv.objects.all()
    form = PersonnelForm()

    context = {'cv': cv, 'form': form}
    "print(form)"
    return render(request, 'index.html', context)
    # return HttpResponse("You're looking at question %s." % text)


def AddPersonelCv(request):

    if request.method == 'POST':
        data = Cv()
        import pdb; pdb.set_trace()
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
        form = PersonnelForm(request.POST,request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.personnel = Personnel.objects.get(id=1)
            instance.save()

            return HttpResponseRedirect('/')
        else:
            errors = form.errors

    cv = Cv.objects.all()
    form = PersonnelForm(request.POST,request.FILES)

    context = {'cv': cv, 'form': form, 'errors': errors}
    return render(request, 'index.html', context)
