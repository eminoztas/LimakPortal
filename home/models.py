from django.db import models
from django.conf import settings
from django.forms import ModelForm,TextInput,Textarea,EmailInput,ImageField,NumberInput,DateInput, DateField, CharField
from cv.models import Cv,Personnel
from ckeditor.widgets import CKEditorWidget
# Create your models here.

class CvForm(ModelForm):

    DateOfBirth = CharField(widget=TextInput(attrs ={'class':'form-control','placeholder':'Dogum Tarihi'}))

    
    class Meta:
        model = Cv
        fields =['FirstName','LastName','DateOfBirth', 'cvImage','EducationalLevel','Adress','Tel','email','Summary']
        widgets = {

            'FirstName' : TextInput(attrs={'class':'form-control','placeholder':'Ad'}),
            'LastName' : TextInput(attrs={'class':'form-control','placeholder':'Soyad'}),
            'EducationalLevel' : TextInput(attrs ={'class':'form-control','placeholder':'Öğrenim durumu'}),
            'Adress' : Textarea(attrs ={'class':'form-control','placeholder':'...'}),
            'Tel' : TextInput(attrs={'class':'form-control','placeholder':'Telefon'}),
            'email' : EmailInput(attrs={'class':'form-control','placeholder':'...'}),
            'Summary' : CKEditorWidget(),
            # 'ozet' : Textarea(attrs={'class':'"ckeditor form-control"','placeholder':'ozet','rows': '6'}),
        }

