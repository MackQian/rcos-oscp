from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=150)
    logo = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    #makes it so then when printing, it prints its name and location
    def __str__(self):
        return self.name+' - '+self.location

class Product(models.Model):
    def __str__(self):
        return self.productName
    productName=models.CharField(max_length=1000)
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=8,decimal_places=2)
