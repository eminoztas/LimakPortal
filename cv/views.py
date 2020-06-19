from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cv(request):
    text ="ilk deneme"
    context = {'txt': text} 
    return render(request, 'cv.html', context)
    # return HttpResponse("You're looking at question %s." % text)