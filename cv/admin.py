from django.contrib import admin

# Register your models here.
from cv.models import Cv,Personnel,Image

class ImageInline(admin.TabularInline):
    model = Image
    extra=5


class CvAdmin(admin.ModelAdmin):
    list_display = ('title','status')
    list_filter = ['status']

class PersonnelAdmin(admin.ModelAdmin):

    list_display = ('titlePersonel','status','image_tag')    
    readonly_fields = ['image_tag']   
    list_filter = ['status']          
    inlines =  [ImageInline]


class ImageAdmin(admin.ModelAdmin):
    list_display = ('personnel','name')


admin.site.register(Cv,CvAdmin)
admin.site.register(Personnel,PersonnelAdmin)
admin.site.register(Image,ImageAdmin)