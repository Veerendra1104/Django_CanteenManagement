from django.db import models

# Create your models here.
class Register_names(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    password = models.TextField(null=True)
    conform_password = models.TextField(null=True)
    
    def __str__(self):
        return self.name


class Registers(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=200)
    conform_password = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
    
class Item(models.Model):
    itemname = models.CharField(max_length=100)
    quantity = models.IntegerField()
    itemcost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.itemname
    