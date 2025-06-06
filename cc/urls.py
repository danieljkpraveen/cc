from cc import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('authentication.urls')),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
