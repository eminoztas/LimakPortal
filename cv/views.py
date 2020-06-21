from django.shortcuts import render
from django.http import HttpResponse
from cv.models import Cv
# Create your views here.

def cv(request):
    cvBilgi = Cv.objects.get(pk=1)
    context = {'cvBilgileri': cvBilgi} 
    return render(request, 'cv.html', context)
    # return HttpResponse("You're looking at question %s." % text)


