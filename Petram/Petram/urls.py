from django.contrib import admin
from django.urls import path
from core.views import HomeView, ContactView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('contato/', ContactView, name='contato'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
