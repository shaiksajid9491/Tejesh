from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20,null=True)
    description=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    name=models.CharField(max_length=20,null=True)
    serialnumber=models.CharField(max_length=20,unique=True)
    price=models.FloatField()
    description = models.CharField(max_length=50, null=True)

    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.name