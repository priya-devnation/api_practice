#Django modules
from django.urls import path

#project modules
from .views import EventListCreateAPIView, EventRetrieveUpdateDeleteAPIView
from .views import BookingListCreateAPIView, BookingRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('',EventListCreateAPIView.as_view(), name='event-list-create'),
    path('<int:pk>/',EventRetrieveUpdateDeleteAPIView.as_view(), name='event-retrieve-update-delete'),
    path('',BookingListCreateAPIView.as_view(), name='booking-list-create'),
    path('<int:pk>/',BookingRetrieveUpdateDeleteAPIView.as_view(), name='booking-retrieve-update-delete'),

]