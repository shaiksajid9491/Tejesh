from django.db import models

from class_based_views.models import BaseModel


# Create your models here.
class Employee(BaseModel):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    age = models.IntegerField()
    salary = models.FloatField()
    address = models.TextField()

    def __str__(self):
        return self.name
