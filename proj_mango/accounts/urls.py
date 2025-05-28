from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login_view'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login_view'), name='logout_view'),
    
    # Register
    path('register/', views.register_view, name='register_view'),
    
    # Profile
    path('profile/', views.profile_view, name='profile_view'),
]


