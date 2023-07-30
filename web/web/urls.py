from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index),
    path('board/', include('board.urls')),
    # path('board/', include('board.urls')),
]
