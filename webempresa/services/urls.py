from django.urls import path
from . import views

urlpatterns = [
    # Paths de core
  
   path('', views.services, name="services"),
  
   
]