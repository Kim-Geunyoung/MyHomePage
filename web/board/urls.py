from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('index/', views.index),
]
