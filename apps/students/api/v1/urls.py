# Django modules
from django.urls import path

# Project modules
from .views import StudentListCreateAPIView, StudentRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('', StudentListCreateAPIView.as_view(), name='student-list-create'), # url for listing and creating students
    path('<int:pk>/', StudentRetrieveUpdateDeleteAPIView.as_view(), name='student-detail-update-delete'), # url for retrieving, updating and deleting a specific student
]
