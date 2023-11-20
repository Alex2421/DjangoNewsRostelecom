from django.urls import path


from . import views
urlpatterns = [
    path('', views.index, name='host'),
    path('about/', views.about, name='about'),
    #path('addpage/', addpage, name='add_page'),
    #path('contact/', contact, name='contact'),
    #path('login/', login, name='login'),
]

