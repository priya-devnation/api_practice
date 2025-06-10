# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/students/', include('apps.students.api.v1.urls')) # Students app
]
