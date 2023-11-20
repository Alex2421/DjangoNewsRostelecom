from django.urls import path


from . import views
urlpatterns = [
    path('', views.index, name='host'),
    path('about/', views.about, name='about'),
    path('plans/', views.plans, name='plans'),
    path('signin/', views.signin, name='signin'),
    #path('login/', login, name='login'),
    #path('contact/', contact, name='contact'),

]

