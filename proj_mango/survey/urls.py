from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey_home_view, name='survey_home'), 
    path('new/', views.create_surveillancerecord_view, name='create_surveillancerecord_view'),
    path('my/', views.my_surveys_view, name='my_surveys_view'),
    path('detail/<int:pk>/', views.survey_detail_view, name='survey_detail_view'),
]
