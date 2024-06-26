from django.contrib import admin
from django.urls import path, include
from pages.urls import pages_patterns

urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include(pages_patterns)),
    path('admin/', admin.site.urls),
    # Paths of Autentication
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')), 
]
