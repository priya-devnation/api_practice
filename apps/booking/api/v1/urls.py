#Django modules
from django.urls import path

#project modules
from .views import BookingListCreateAPIView, BookingRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('',BookingListCreateAPIView.as_view(), name='booking-list-create'),     #for listing and creating booking data
    path('<int:pk>/',BookingRetrieveUpdateDeleteAPIView.as_view(), name='booking-retrieve-update-delete'),    #for updating, deleting and retrieving booking data

]