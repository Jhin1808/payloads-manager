from django.urls import path
from .import views

urlpatterns = [
    path("parts/", views.parts_list, name="parts_list")
]