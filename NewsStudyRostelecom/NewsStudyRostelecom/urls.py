from django.contrib import admin
from django.urls import path
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('main.urls'))
    #патф для хоум
    #path('home/', include('home.urls'))
    #path('yummy/', include('yummy.urls'))
    path('host/', include('host.urls'))
]
