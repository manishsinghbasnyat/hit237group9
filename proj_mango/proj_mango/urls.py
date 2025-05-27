from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    
    # For catalog
    path('', include('catalog.urls')),  # All catalog routes (home, pests, about, etc.)
    
     # For survey
     path('survey/', include('survey.urls')),
     
     # For accounts
     path('', include('accounts.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)