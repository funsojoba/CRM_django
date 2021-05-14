from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('index.html/', views.home),
    path('products/', views.products),
    path('customer/', views.customer)
]