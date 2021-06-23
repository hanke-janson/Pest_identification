from django.urls import path
from apps.pest import views

urlpatterns = [
    path('index/', views.visualization),
]
