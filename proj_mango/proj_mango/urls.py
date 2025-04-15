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

    # Home page route
    path('', views.home, name='home'),
    
    # Pest/Disease list page
    path('pests/', views.pest_list_view, name='pest_list'),
    
    # Pest/Disease detail page, using the item_id as a dynamic URL parameter
    path('pest/<int:item_id>/', views.pest_detail_view, name='pest_detail'),
    
    # About page route
    path('about/', views.about, name='about'),
    
    # References page route
    path('references/', views.references, name='references'),
]


