from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'host/index.html')
def about(request):
    return render(request, 'host/about.html')
def plans(request):
    return render(request, 'host/plans.html')