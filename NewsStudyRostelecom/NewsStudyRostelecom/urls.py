from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from host.views import page_not_found
#import host.views as host_views
handler404 = 'host.views.not_found_view'

from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('main.urls')), #отключил для выгрузки на гит
    path('news/', include('news.urls')),
    path('users/', include('users.urls')),
    path('', include('host.urls')),
    #path('host/', include('host.urls')),
    path('home/', include('home.urls')),
    #htpp://127.0.0.1:8000/


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

