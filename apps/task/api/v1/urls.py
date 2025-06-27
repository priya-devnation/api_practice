# Django modules
from django.urls import path

# Project modules
from .views import TaskCreateAPIView,TaskListAPIView, TaskRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('', TaskCreateAPIView.as_view(), name='task-create'), # url for  creating tasks
    path('list/', TaskListAPIView.as_view(), name='task-list'), # url for  listing tasks
    path('<int:pk>/', TaskRetrieveUpdateDeleteAPIView.as_view(), name='task-detail-update-delete'), # url for retrieving, updating and deleting a specific task
]
