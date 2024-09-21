from django.urls import path
from . import views

urlpatterns = [
    path('', views.stop_list, name='stop_list'),
    path('stop/<int:pk>/', views.stop_detail, name='stop_detail'),
    path('search/', views.search_stops, name='search_stops'),
    path('creer-ligne/', views.creer_ligne, name='creer_ligne'),
]