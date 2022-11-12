from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.name