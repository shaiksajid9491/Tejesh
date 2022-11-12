from django.contrib import admin
from django.urls import path, include

from .views import employee_list_create, employee_update_delete

urlpatterns = [
    path('employee/', employee_list_create, name="employee_list_create"),
    path("employee/<int:pk>",employee_update_delete, name="employee_update_delete")
]