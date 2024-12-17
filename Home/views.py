from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def  index(request):
    return render(request,'home/index.html') # Ici on indique clairement le chemin du fichier index.html