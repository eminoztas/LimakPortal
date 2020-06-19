from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('deneme', views.cv, name='cv'),
]