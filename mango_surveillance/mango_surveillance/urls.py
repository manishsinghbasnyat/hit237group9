"""
URL configuration for mango_surveillance project.

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
# mango_surveillance/urls.py
# mango_surveillance/urls.py
from django.contrib import admin
from django.urls import path
from app_pests import views  # Make sure to import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('pests/', views.pests_list_view, name='pests_list'),
    path('pests/<int:id>/', views.pest_detail_view, name='pest_detail'),
    path('about/', views.about_view, name='about'),  # Add this line for the About page
]
