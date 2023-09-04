from django.urls import path
from . import views

urlpatterns = [
    path('allplaces/', views.all_places_view, name="all_places")
]
