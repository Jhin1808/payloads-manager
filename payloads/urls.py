from django.urls import path
from .import views

urlpatterns = [
    path("parts/", views.parts_list, name="parts_list"),
    path("parts/<int:pk>/", views.part_detail, name="part_detail"),

    
]