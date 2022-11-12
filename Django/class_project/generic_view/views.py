from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Employee
from .serializers import EmployeeSerializers


# Create your views here.


class employee_list_create(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    permission_classes = [permissions.AllowAny]


class employee_update_delete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    permission_classes = [permissions.AllowAny]