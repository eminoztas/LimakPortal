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
    personnel = models.ForeignKey(Personnel,on_delete=models.CASCADE) 
    FirstName = models.CharField(blank=True,max_length=50)
    LastName = models.CharField(blank=True,max_length=50)
    DateOfBirth = models.DateField(editable=True, blank=True)
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


class Image(models.Model):

    personnel = models.ForeignKey(Personnel,on_delete=models.CASCADE)
    image = models.ImageField(blank=True,upload_to='images/')
    name = models.CharField(max_length=70)
    create_time=models.DateField(auto_now_add=True)
    update_time=models.DateField(auto_now=True) 

    def __str__(self):
        return self.name