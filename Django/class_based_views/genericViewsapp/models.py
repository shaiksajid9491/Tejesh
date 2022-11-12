from django.db import models

from class_based_views.models import BaseModel


# Create your models here.
class Student(BaseModel):
    name = models.CharField(max_length=80)
    contact = models.CharField(max_length=10)
    age = models.IntegerField()
    branch = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name