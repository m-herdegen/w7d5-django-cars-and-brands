from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100, null=True)

class Car(models.Model):
    name = models.CharField(max_length=100, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True) 
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)