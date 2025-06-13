
# Django modules
from django.urls import path

#project modules
from .views import TodoListCreateAPIView, TodoRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('', TodoListCreateAPIView.as_view(), name='todo-list-create'), # url for listing and creating data in todo
    path('<int:pk>/',TodoRetrieveUpdateDeleteAPIView.as_view(), name='todo-retrieve-update-delete'), # url for retrieving, updating and deleting a specific data from todo 
]

