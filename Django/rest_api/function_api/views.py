from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Employee
from .serializers import EmployeeSerializers


# Create your views here.


@api_view(['GET','POST'])
def employee_list_create(request):
    if request.method == "GET":
        emp_obj = Employee.objects.all()
        serializers_obj = EmployeeSerializers(emp_obj, many=True)
        return Response(serializers_obj.data, status=status.HTTP_200_OK)
    else:
        serializer_obj = EmployeeSerializers(data=request.data)
        if serializer_obj.is_valid(raise_exception=True):
            serializer_obj.save()
        return Response(serializer_obj.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def employee_update_delete(request, pk):

    employee_obj = get_object_or_404(Employee, id=pk)

    if request.method == "GET":
        serializer_obj = EmployeeSerializers(employee_obj)
        return Response(serializer_obj.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer_obj = EmployeeSerializers(instance=employee_obj, data=request.data)
        if serializer_obj.is_valid(raise_exception=True):
            serializer_obj.save()
            return Response(serializer_obj.data, status=status.HTTP_200_OK)

    if request.method == "DELETE":
        employee_obj.delete()
        return Response({'msg': 'done'}, status=status.HTTP_204_NO_CONTENT)












