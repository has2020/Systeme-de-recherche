from django.shortcuts import render
from django.http import HttpResponse,Http404
from catalog.models import Document
# Create your views here.
def texte(request):
        if request.method == 'POST':
            if request.POST.get('description', False):
                description = str(request.POST['description'])      
                #watch your command line
                print(description)
            if request.POST.get('name', False):
                name = str(request.POST['name'])
            if request.POST.get('num', False):
                num = str(request.POST['num']) 
        return render(request,'catalog/texte.html',locals())
