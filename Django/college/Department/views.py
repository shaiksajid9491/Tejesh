from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher
from .searializers import TeacherSerializers


# Create your views here.


def home(request):
    return HttpResponse("Hello World")


class TeacherCurd(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            name_records = request.query_params.get("name", None)
            salary_records = request.query_params.get("salary", None)
            age_records = request.query_params.get("age", None)

            if name_records:
                queryset = queryset.filter(name=name_records)

            if salary_records:
                queryset = queryset.filter(salary__gt=salary_records)

            if age_records:
                queryset = queryset.filter(age__gt=age_records)

            serializer_data = self.get_serializer(queryset, many=True).data

            return Response(
                data={
                    'message': 'details displayed successfully',
                    'details': serializer_data,
                    'success': True
                },
                status=status.HTTP_200_OK

            )
        except Exception as error:
            return Response(
                {"massage": str(error)}, status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request, *args, **kwargs):
        data = request.data
        try:

            with transaction.atomic():

                teach_name = data.get("name", None)

                if teach_name and Teacher.objects.filter(name=teach_name).exists():
                    raise Exception("already this username is taken choose different name")

                tearcher_record = Teacher.objects.create(
                    name=teach_name,
                    address=data.get("address", None),
                    age=data.get("age", None),
                    salary=data.get("salary", None)

                )
                serializer_data = self.get_serializer(tearcher_record).data

                return Response(
                    data={
                        "massage": "Details added successfully",
                        "details": serializer_data,
                        "success": True

                    },
                    status= status.HTTP_201_CREATED
                )
        except Exception as error:

            return Response(
                {"message": str(error)}, status=status.HTTP_400_BAD_REQUEST
            )





    def destroy(self, request, *args, **kwargs):

        try:
            with transaction.atomic():

                teacher_record = self.get_object()
                if teacher_record:
                    teacher_record.delete()

                serializer_data = self.get_serializer(teacher_record).data

                return Response(
                    data = {
                        "massage":"teacher_record deleted successfully",
                        "Details":serializer_data,
                        "success":True
                    },
                    status=status.HTTP_204_NO_CONTENT
                )

        except Exception as error:
            return Response(
                {"massage":str(error)},status=status.HTTP_400_BAD_REQUEST
            )



    def partial_update(self, request, *args, **kwargs):
        data = request.data

        try:

            with transaction.atomic():
                teacher_record = self.get_object()

                if teacher_record:

                    teacher_record.name = data.get("name"),
                    teacher_record.address = data.get("address"),
                    teacher_record.age = data.get("age"),
                    teacher_record.salary = data.get("salary")
                    teacher_record.save()

                serializer_data = self.get_serializer(teacher_record).data

                return Response(
                    data = {
                        "message":"Details updated successfully",
                        "details":serializer_data,
                        "success":True

                    },
                    status=status.HTTP_200_OK
                )
        except Exception as error:
            return  Response(
                {"massage":str(error)},status=status.HTTP_400_BAD_REQUEST
            )

