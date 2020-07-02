from django.db import models
from django.conf import settings
from django.forms import ModelForm,TextInput,Textarea,EmailInput,ImageField,NumberInput,DateInput, DateField, CharField,HiddenInput
from cv.models import Cv,Personnel,WorkExperiences,Certifications,Languages
from ckeditor.widgets import CKEditorWidget
# Create your models here.

class CvForm(ModelForm):

    DateOfBirth = CharField(widget=TextInput(attrs ={'class':'form-control','placeholder':'Dogum Tarihi'}))

    
    class Meta:
        model = Cv
        fields =['ID','FirstName','LastName', 'DateOfBirth', 'cvImage','EducationalLevel','Summary','Tel','email']
        widgets = {
            'ID' : HiddenInput(),
            'FirstName' : TextInput(attrs={'class':'form-control','placeholder':'Ad'}),
            'LastName' : TextInput(attrs={'class':'form-control','placeholder':'Soyad'}),
            'EducationalLevel' : TextInput(attrs ={'class':'form-control','placeholder':'Öğrenim durumu'}),
            'Adress' : Textarea(attrs ={'class':'form-control','placeholder':'...'}),
            'Tel' : TextInput(attrs={'class':'form-control','placeholder':'Telefon'}),
            'email' : EmailInput(attrs={'class':'form-control','placeholder':'...'}),
            'Summary' : CKEditorWidget(),
            # 'ozet' : Textarea(attrs={'class':'"ckeditor form-control"','placeholder':'ozet','rows': '6'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(CvForm, self).__init__(*args, **kwargs)
        self.fields['ID'].required = False


class WorkExperiencesForm(ModelForm):
        
    class Meta:
        model = WorkExperiences
        fields =['ID','WorkExperienceName','Title', 'FromYear', 'ToYear','Description']
        widgets = {
            'ID' : HiddenInput(),
            'WorkExperienceName' : TextInput(attrs={'class':'form-control','placeholder':'..'}),
            'Title' : TextInput(attrs={'class':'form-control','placeholder':'..'}),
            'ToYear' : TextInput(attrs ={'class':'form-control','placeholder':'...'}),
            'FromYear' : TextInput(attrs ={'class':'form-control','placeholder':'..'}),
            'Description' : Textarea(attrs ={'class':'form-control','placeholder':'...'}),
        }

    def __init__(self, *args, **kwargs):
        super(WorkExperiencesForm, self).__init__(*args, **kwargs)
        self.fields['ID'].required = False

class CertificationsForm(ModelForm):
        
    class Meta:
        model = Certifications
        fields =['ID','CertificationName','CertificationAuthority', 'FromYear', 'ToYear']
        widgets = {
            'ID' : HiddenInput(),
            'CertificationName' : TextInput(attrs={'class':'form-control','placeholder':'..'}),
            'CertificationAuthority' : TextInput(attrs={'class':'form-control','placeholder':'Soy..ad'}),
            'ToYear' : TextInput(attrs ={'class':'form-control','placeholder':'...'}),
            'FromYear' : TextInput(attrs ={'class':'form-control','placeholder':'..'}),
        }


    def __init__(self, *args, **kwargs):
        super(CertificationsForm, self).__init__(*args, **kwargs)
        self.fields['ID'].required = False

        
class LanguagesForm(ModelForm):
        
    class Meta:
        model = Languages
        fields =['ID','LanguageName','LanguageLevel']
        widgets = {
            'ID' : HiddenInput(),
            'LanguageName' : TextInput(attrs={'class':'form-control','placeholder':'..'}),
            'LanguageLevel' : TextInput(attrs={'class':'form-control','placeholder':'...'}),
        }

    def __init__(self, *args, **kwargs):
        super(LanguagesForm, self).__init__(*args, **kwargs)
        self.fields['ID'].required = False
