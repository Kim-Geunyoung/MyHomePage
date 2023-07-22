from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('board/', views.index),
]
