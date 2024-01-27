from django.contrib import admin
from django.urls import path
from searchapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('champions/', views.champions),
]
