from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('CvKaydet', views.CvAPIView.as_view())
    # path('AddPersonelCv', views.AddPersonelCv, name='AddPersoneCv'),
]