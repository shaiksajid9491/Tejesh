from django.shortcuts import render, get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Department
from .serializers import DepartmentSerializers


# Create your views here.



class department_curd(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None, format=None):
        if pk:
            student = get_object_or_404(Department, id=pk)
            student_serializers = DepartmentSerializers(student)
            return Response(student_serializers.data, status=status.HTTP_200_OK)
        else:
            students_qs = Department.objects.all()
            student_serializers = DepartmentSerializers(students_qs, many=True)
            return Response(student_serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        student_serializers = DepartmentSerializers(data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None, format=None):
        student = get_object_or_404(Department, id=pk)
        student_serializers = DepartmentSerializers(instance=student, data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_200_OK)

    def delete(self,request, pk=None, format=None):
        student = get_object_or_404(Department, id=pk)
        student.delete()
        return Response({'msg': 'done'}, status=status.HTTP_204_NO_CONTENT)