from django.urls import path
from .import views

urlpatterns = [
    path("parts/", views.part_list, name="parts_list")
]