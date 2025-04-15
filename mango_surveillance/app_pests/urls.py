# app_pests/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('pests/', views.pests_list_view, name='pests_list'),
    path('pests/<int:id>/', views.pest_detail_view, name='pest_detail'),  # This line enables pest detail view
]
