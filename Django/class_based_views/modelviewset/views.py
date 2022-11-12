from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Employee
from .serializer import EmployeeSerializers


# Create your views here.
class EmployeeCurd(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    permission_classes = [permissions.AllowAny]
