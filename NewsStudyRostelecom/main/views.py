from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse('<h1> Ура, работает! </h1>')
   return  render(request, 'main/index.html')

def sidebar(request):
   return  render(request, 'main/sidebar.html')