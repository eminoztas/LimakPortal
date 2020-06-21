from django.db import models
from django.forms import ModelForm,TextInput,Textarea,EmailInput,ImageField
from cv.models import Cv,Personnel
from ckeditor.widgets import CKEditorWidget
# Create your models here.

class PersonnelForm(ModelForm):
    class Meta:
        model = Cv
        fields =['name','surname','email','title','description','cvImage','telefon','ozet']
        widgets = {

            'name' : TextInput(attrs={'class':'form-control','placeholder':'Ad'}),
            'surname' : TextInput(attrs={'class':'form-control','placeholder':'Soyad'}),
            'email' : EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'title' : TextInput(attrs={'class':'form-control','placeholder':'title'}),
            'description' : Textarea(attrs={'class':'form-control','placeholder':'description'}),
            # 'ozet' : Textarea(attrs={'class':'"ckeditor form-control"','placeholder':'ozet','rows': '6'}),
            'ozet' : CKEditorWidget(),
            'telefon' : TextInput(attrs={'class':'form-control','placeholder':'telefon'}),
        }

