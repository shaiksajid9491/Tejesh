from django.shortcuts import render
from rest_framework import viewsets, generics, permissions

from .models import Student
from .serializer import StudentSerializers


# Create your views here.
class StudentCurd(viewsets.ViewSetMixin, generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [permissions.AllowAny]
