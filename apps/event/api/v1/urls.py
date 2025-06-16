#Django modules
from django.urls import path

#project modules
from .views import EventListCreateAPIView, EventRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('',EventListCreateAPIView.as_view(), name='event-list-create'),   #for listing and creating events
    path('<int:pk>/',EventRetrieveUpdateDeleteAPIView.as_view(), name='event-retrieve-update-delete'),    #for updating,deleting and retrieving 
]