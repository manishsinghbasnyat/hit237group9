from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.create_surveillancerecord_view, name='create_surveillancerecord_view'),
]
