# Project modules
from django.urls import path
from .views import EmployeeListCreateAPIView, EmployeeRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('', EmployeeListCreateAPIView.as_view(), name='employee-list-create'), # url for listing and creating employees
    path('<uuid:uuid>/', EmployeeRetrieveUpdateDeleteAPIView.as_view(), name='employee-detail-update-delete'), # url for retrieving, updating and deleting an employee
]