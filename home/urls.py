from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('personnelCv',views.CvListele,name='CvListele'),
    # path('AddPersonelCv', views.AddPersonelCv2, name='AddPersoneCv'),
    # path('AddPersonelCv', views.AddPersonelCv, name='AddPersoneCv'),
    path('AddPersonelCv', views.AddPersonelCv3, name='AddPersoneCv'),
]