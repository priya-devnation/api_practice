# Django modules
from django.urls import path

# Project modules
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('', TaskListCreateAPIView.as_view(), name='student-list-create'), # url for listing and creating tasks
    path('<int:pk>/', TaskRetrieveUpdateDeleteAPIView.as_view(), name='student-detail-update-delete'), # url for retrieving, updating and deleting a specific task
]
