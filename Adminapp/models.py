from django.db import models

# Create your models here.
class Categories(models.Model):
    Name = models.CharField(max_length = 200)
    Image = models.ImageField(upload_to='images')
    Description = models.CharField(max_length = 200)

class Products(models.Model):
    Name = models.CharField(max_length = 200)
    Category = models.CharField(max_length = 200 , default = '')
    Image = models.ImageField(upload_to='images')
    Price = models.CharField(max_length = 200)
    Quantity = models.CharField(max_length = 200)

