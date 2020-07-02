from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.http import HttpResponseRedirect
from cv.models import Cv, Personnel,YeniCv
from home.models import CvForm,WorkExperiencesForm,CertificationsForm,LanguagesForm
from django import forms
import requests
import json



# Create your views here.
def index(request):
    form2 = WorkExperiencesForm()
    form = CvForm()
    form3 = CertificationsForm()
    form4 = LanguagesForm()
    context = { 'form': form,'form2':form2, 'form3':form3, 'form4':form4}
    "print(form)"
    return render(request, 'index.html', context)
    # return HttpResponse("You're looking at question %s." % text)


def AddPersonelCv(request):

    if request.method == 'POST':
        data = CvForm()
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
    form2 = WorkExperiencesForm(request.POST)
    form3 = CertificationsForm(request.POST)
    form4 = LanguagesForm(request.POST)
    api_url ='https://limakcv.herokuapp.com/persons'
    if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
        received_json_data = json.loads(json.dumps(form.cleaned_data))
        del received_json_data['ID']
        response = requests.post(api_url, json=received_json_data)
        if response.status_code != 201:
            import pdb; pdb.set_trace()
        else:
            sonuc = response.json()
            api_url = 'https://limakcv.herokuapp.com/persons/' + str(sonuc["ID"]) + '/workexperiences'
            received_json_data2 = json.loads(json.dumps(form2.cleaned_data))
            del received_json_data2['ID']
            response = requests.post(api_url, json=received_json_data2)
            api_url = 'https://limakcv.herokuapp.com/persons/' + str(sonuc["ID"]) + '/certifications'
            received_json_data3 = json.loads(json.dumps(form3.cleaned_data))
            del received_json_data3['ID']
            response = requests.post(api_url, json=received_json_data3)
            api_url = 'https://limakcv.herokuapp.com/persons/' + str(sonuc["ID"]) + '/languages'
            received_json_data4 = json.loads(json.dumps(form4.cleaned_data))
            del received_json_data4['ID']
            response = requests.post(api_url, json=received_json_data4)
            return HttpResponseRedirect('/personnelCv')
        # import pdb; pdb.set_trace()
    else:
        print(form.errors)
        return HttpResponseRedirect('/personnelCv')
    return render(request, 'index.html', {})


def CvListele(request):
    api_url = 'https://limakcv.herokuapp.com/persons'
    response = requests.get(api_url)
    cvlist = []
    cv_data = response.json()
    for c in cv_data:
        cvlist.append(YeniCv(**c))
        "print(form)"
    return render(request,"personnelCv.html",{'items': cvlist})
    
 
def Edit(request, object_id):
    api_url = 'https://limakcv.herokuapp.com/persons/' + str(object_id)
    response = requests.get(api_url)
    cv_data = response.json()
    for item in cv_data["WorkExperiences"]:   
        form2 = WorkExperiencesForm(initial=item)
    for item in cv_data["Certifications"]:   
        form3 = CertificationsForm(initial=item) 
    for item in cv_data["Languages"]:   
        form4 = LanguagesForm(initial=item)  
    form = CvForm(initial=cv_data)
    print("Errors", form.errors)
    context = {'form': form,'form2': form2,'form3':form3,'form4':form4}
    print(form)
    return render(request, 'contentEdit.html', context)
    

def ContentEdit(request, object_id):
    api_url = 'https://limakcv.herokuapp.com/persons/' + str(object_id)
    form = CvForm(request.POST) 
    form2 = WorkExperiencesForm(request.POST)
    form3 = CertificationsForm(request.POST)
    form4 = LanguagesForm(request.POST)
    if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
        received_json_data = json.loads(json.dumps(form.cleaned_data)) 
        del received_json_data['ID']
        response = requests.put(api_url, json=received_json_data)
        if response.status_code != 200:
            import pdb; pdb.set_trace()
        else:
            
            received_json_data2 = json.loads(json.dumps(form2.cleaned_data))
            
            api_url = 'https://limakcv.herokuapp.com/persons/' + str(object_id) + '/workexperiences/' + str(received_json_data2["ID"])
            del received_json_data2['ID']
            
            response = requests.put(api_url, json=received_json_data2)
            received_json_data3 = json.loads(json.dumps(form3.cleaned_data))
            
            api_url = 'https://limakcv.herokuapp.com/persons/' + str(object_id) + '/certifications/' + str(received_json_data3["ID"])
            del received_json_data3['ID']
            
            response = requests.put(api_url, json=received_json_data3)

            received_json_data4 = json.loads(json.dumps(form4.cleaned_data))
         
            api_url = 'https://limakcv.herokuapp.com/persons/' + str(object_id) + '/languages/' + str(received_json_data4["ID"])
            del received_json_data4['ID']
            
            response = requests.put(api_url, json=received_json_data4)
            return HttpResponseRedirect('/personnelCv')
        # import pdb; pdb.set_trace()
    else:
        print(form.errors)


def Delete(request, object_id):
    api_url = 'https://limakcv.herokuapp.com/persons/' + str(object_id)
    requests.delete(api_url)
    return HttpResponseRedirect('/personnelCv')

    
    # return render(request, 'index.html', {})
    # response = requests.get(api_url)
    # cv_data = response.json()
    # form = CvForm(initial=cv_data)
    # print("Errors", form.errors)
    # # import pdb ; pdb.set_trace()
    # context = {'form': form}
    # print(form)
    # return render(request, 'contentEdit.html', context)
     


    # new_cv = Cv()
    # for key, value in cv_data.items():
    #     setattr(new_cv, key, value)
    