# Django modules
from django.urls import path

# Project modules
from .views import (
    HolidayListCreateAPIView, 
    HolidayRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('', HolidayListCreateAPIView.as_view(), name='holiday-list-create'),  # URL for creating and listing holiday
    path('<int:pk>/', HolidayRetrieveUpdateDestroyAPIView.as_view(), name='holiday-retrieve-update-destroy'), # URL for retrieving, updating and deleting holiday
]