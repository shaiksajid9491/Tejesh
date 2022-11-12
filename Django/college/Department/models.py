from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    # contact = models.CharField(max_length=10)
    address = models.TextField()
    age = models.IntegerField()
    salary = models.FloatField()