from django.db import models
from Adminapp.models import*
# Create your models here.
class Contact (models.Model):
    Name = models.CharField(max_length = 10)
    Mail = models.EmailField()
    Number = models.IntegerField()
    Message = models.CharField(max_length = 150)

class Register (models.Model):
    Username = models.CharField(max_length = 10)
    Mail = models.EmailField()
    Number = models.IntegerField()
    Password = models.CharField(max_length = 10)

class Cart(models.Model):
    userid = models.ForeignKey(Register,on_delete= models.CASCADE)
    productid = models.ForeignKey(Products , on_delete = models.CASCADE)
    quantity  = models.IntegerField()
    total = models.IntegerField()
    status = models.IntegerField(default = 0)

class Checkout(models.Model):
    userid = models.ForeignKey(Register , on_delete = models.CASCADE)
    cartid = models.ForeignKey(Cart , on_delete = models.CASCADE)
    Country = models.CharField(max_length = 200)
    State = models.CharField(max_length = 200)
    Address = models.CharField(max_length = 200)
    City = models.CharField(max_length = 200)
    Postcode = models.CharField(max_length = 200)