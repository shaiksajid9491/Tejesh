from rest_framework.serializers import ModelSerializer

from .models import Student


class StudentSerializers(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

