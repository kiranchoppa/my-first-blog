from django.urls import path
from . import views

urlpatterns = [
    path("", views.available_items, name="available_items"),
]
