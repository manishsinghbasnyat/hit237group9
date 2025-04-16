from django.contrib import admin
from django.urls import path
from app_mango import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # -- my urls -- #

   # Home page (Introduction and overview)
    path('', views.home, name='home'),
<<<<<<< HEAD

    # Combined Pest & Disease List
    path('pests-diseases/', views.pest_disease_list, name='pest_disease_list'),

    # Individual Pest Detail Page
    path('detail/pest/<int:pest_id>/', views.pest_detail, name='pest_detail'),

    # Individual Disease Detail Page
    path('detail/disease/<int:disease_id>/', views.disease_detail, name='disease_detail'),

    # About page (Team details)
=======
    
    # Pest/Disease list page
    path('pests/', views.pest_list_view, name='pest_list'),
    
    # Pest/Disease detail page, using the item_type (pest or disease) and item_id
    path('<str:item_type>/<int:item_id>/', views.pest_detail_view, name='pest_detail'),
    
    # About page route
>>>>>>> main
    path('about/', views.about, name='about'),
]
