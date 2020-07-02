from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.CvListele, name='index'),
    path('Anasayfa', views.index, name='index'),
    path('personnelCv',views.CvListele,name='CvListele'),
    # path('AddPersonelCv', views.AddPersonelCv2, name='AddPersoneCv'),
    # path('AddPersonelCv', views.AddPersonelCv, name='AddPersoneCv'),
    path('AddPersonelCv', views.AddPersonelCv3, name='AddPersoneCv'),
    path('edit/<int:object_id>', views.Edit, name='edit'),
    path('edit/ContentEdit/<int:object_id>', views.ContentEdit, name='ContentEdit'),
    path('delete/<int:object_id>', views.Delete, name='Delete'),
]