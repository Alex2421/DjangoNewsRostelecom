from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import main.views as main_views
#handler404 = main_views.custom_404
from django.conf import settings
urlpatterns = [
     path('admin/', admin.site.urls),
     path('',include('main.urls')),
     path('home/', include('home.urls')),
     path('host/', include('host.urls')),
#     htpp://127.0.0.1:8000/

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)