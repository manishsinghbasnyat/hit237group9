from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pests/', views.pest_list_view, name='pest_list'),
    path('<str:item_type>/<int:item_id>/', views.pest_detail_view, name='pest_detail'),
    path('about/', views.about, name='about'),
    path('references/', views.references, name='references'),
]
