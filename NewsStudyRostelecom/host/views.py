from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect


def index(request):
    return render(request, 'host/index.html')
def about(request):
    return render(request, 'host/about.html')
def plans(request):
    return render(request, 'host/plans.html')
def signin(request):
    return render(request, 'host/sign-in.html'),

#def custom_404(request, exception):
#   return render(request, ‘host/404.html’, status=404)

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Ой, что-то пошло не так. Страница не найдена!</h1>')
