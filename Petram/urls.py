from django.contrib import admin
from django.urls import path
from core.views import home_view
from django.conf.urls.static import static
from django.conf import settings

app_name = 'petram'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
