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
    
    # Pest/Disease detail page, using the item_type (pest or disease) and item_id
    path('<str:item_type>/<int:item_id>/', views.pest_detail_view, name='pest_detail'),
    
    # About page route
    path('about/', views.about, name='about'),
    
    # References page route
    path('references/', views.references, name='references'),
]
