from django.urls import path
from . import views

urlpatterns = [
    # Paths de pages
   path('<int:page_id>/', views.page, name="page"),
]
