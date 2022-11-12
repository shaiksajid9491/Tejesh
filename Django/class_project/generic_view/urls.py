




from django.contrib import admin
from django.urls import path, include

from .views import employee_list_create, employee_update_delete

urlpatterns = [
    path('employee', employee_list_create.as_view()),
    path('employee/<int:pk>/',employee_update_delete.as_view())

]