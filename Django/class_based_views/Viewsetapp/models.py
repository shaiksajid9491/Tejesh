from django.db import models


from class_based_views.models import BaseModel


class Department(BaseModel):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.name