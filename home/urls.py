from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('AddPersoneCv/', views.AddPersonelCv, name='AddPersoneCv'),
]