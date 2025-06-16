# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/students/', include('apps.students.api.v1.urls')), # Students app
    path('api/v1/todo/', include('apps.todo.api.v1.urls')), # todo app
    path('api/v1/holiday/', include('apps.holiday.api.v1.urls')), # holiday app
    path('api/v1/booking/', include('apps.booking.api.v1.urls')), # booking app
 ]


