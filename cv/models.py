from django.db import models
from django.utils.safestring import mark_safe
from datetime import date
from phone_field import PhoneField



class Personnel(models.Model):  
    
    parent = models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    personelName= models.CharField(max_length=50)
    titlePersonel = models.CharField(max_length=50)
    keywords = models.CharField(max_length=200)
    description =models.CharField(max_length=200)
    personelImage = models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=10)
    slug =models.SlugField()
    create_time=models.DateField(auto_now_add=True)
    update_time=models.DateField(auto_now=True) 

    def __str__(self):
        return self.titlePersonel

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.personelImage.url))
    image_tag.short_descrption ='Image'


class Cv(models.Model):
    ID = models.CharField(max_length=5)
    FirstName = models.CharField(blank=True,max_length=50)
    LastName = models.CharField(blank=True,max_length=50)
    DateOfBirth = models.DateField(editable=True, blank=True, null=True)
    email = models.EmailField(blank=True,max_length=13)
    Tel = models.CharField(blank=True,max_length=16)  
    Summary = models.CharField(blank=True,max_length=200)
    cvImage = models.ImageField(blank=True,upload_to='images/')
    EducationalLevel = models.CharField(blank=True,max_length=10)
    Adress = models.CharField(blank=True,max_length=100)
    # create_time=models.DateField(auto_now_add=True)
    # update_time=models.DateField(auto_now=True) 
    # slug =models.SlugField()
   
    def __str__(self):
        return self.FirstName


class WorkExperiences(models.Model):
    ID = models.CharField(max_length=5)
    WorkExperienceName = models.CharField(max_length=70,blank=True,null=True)
    Title = models.CharField(max_length=70,blank=True,null=True)
    FromYear = models.CharField(max_length=70,blank=True,null=True)
    ToYear = models.CharField(max_length=70,blank=True,null=True)
    Description = models.CharField(max_length=70,blank=True,null=True)

    def __str__(self):
        return self.WorkExperienceName

class Certifications(models.Model):
    ID = models.CharField(max_length=5)
    CertificationName = models.CharField(max_length=70,blank=True,null=True)
    CertificationAuthority = models.CharField(max_length=70,blank=True,null=True)
    FromYear = models.CharField(max_length=70,blank=True,null=True)
    ToYear = models.CharField(max_length=70,blank=True,null=True)

    def __str__(self):
        return self.CertificationName

class Languages(models.Model):
    ID = models.CharField(max_length=5)
    LanguageName = models.CharField(max_length=70,blank=True,null=True)
    LanguageLevel = models.CharField(max_length=70,blank=True,null=True)

    def __str__(self):
        return self.LanguageName


class Image(models.Model):

    personnel = models.ForeignKey(Personnel,on_delete=models.CASCADE)
    image = models.ImageField(blank=True,upload_to='images/')
    name = models.CharField(max_length=70)
    create_time=models.DateField(auto_now_add=True)
    update_time=models.DateField(auto_now=True) 

    def __str__(self):
        return self.name


class YeniCv:     
    def __init__(self,ID,CreatedAt,UpdatedAt,DeletedAt,FirstName,LastName,DateOfBirth,EducationalLevel,Adress,Tel,Email,Summary,WorkExperiences,Skills,Certifications,Languages):
         self.ID = ID
         self.CreatedAt = CreatedAt
         self.UpdatedAt = UpdatedAt
         self.DeletedAt = DeletedAt
         self.FirstName = FirstName
         self.LastName = LastName
         self.DateOfBirth = DateOfBirth
         self.EducationalLevel = EducationalLevel
         self.Adress = Adress
         self.Tel = Tel
         self.Email = Email
         self.Summary = Summary        