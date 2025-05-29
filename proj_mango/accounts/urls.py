from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login_view'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login_view'), name='logout_view'),

    # User registration
    path('register/', views.register_view, name='register_view'),

    # Farm CRUD
    path('farms/add/', views.add_farm_view, name='add_farm_view'),                                 # Create
    path('farms/<int:pk>/', views.farm_detail_view, name='farm_detail'),                           # Read
    path('farms/<int:pk>/edit/', views.farm_update_view, name='farm_update_view'),                 # Update
    path('farms/<int:pk>/delete/', views.farm_confirm_delete_view, name='farm_delete_view'),       # Delete
]
