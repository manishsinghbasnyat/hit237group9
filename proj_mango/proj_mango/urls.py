"""
URL configuration for proj_mango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_mango import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    # -- my urls -- #

   # Home page (Introduction and overview)
    path('', views.home, name='home'),

    # Combined Pest & Disease List
    path('pests-diseases/', views.pest_disease_list, name='pest_disease_list'),

    # Individual Pest Detail Page
    path('detail/pest/<int:pest_id>/', views.pest_detail, name='pest_detail'),

    # Individual Disease Detail Page
    path('detail/disease/<int:disease_id>/', views.disease_detail, name='disease_detail'),

    # About page (Team details)
    path('about/', views.about, name='about'),
]


