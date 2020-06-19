from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    text ="ilk deneme"
    context = {'txt': text} 
    return render(request, 'index.html', context)
    # return HttpResponse("You're looking at question %s." % text)