from django.urls import path
from apps.uav import views

urlpatterns = [
    path('index/', views.visualization)
]
