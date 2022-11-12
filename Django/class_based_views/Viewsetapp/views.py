from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import Department
from .serializer import DepartmentSerializers


# Create your views here.
class DepartmentCurd(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        students_qs = Department.objects.all()
        student_serializers = DepartmentSerializers(students_qs, many=True)
        return Response(student_serializers.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        student = get_object_or_404(Department, id=pk)
        student_serializers = DepartmentSerializers(student)
        return Response(student_serializers.data, status=status.HTTP_200_OK)

    def create(self, request):
        student_serializers = DepartmentSerializers(data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, ):
        student = get_object_or_404(Department, id=pk)
        student_serializers = DepartmentSerializers(instance=student, data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None, ):
        student = get_object_or_404(Department, id=pk)
        student.delete()
        return Response({'msg': 'done'}, status=status.HTTP_204_NO_CONTENT)
