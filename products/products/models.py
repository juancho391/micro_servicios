from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=15)



class Product(models.Model):
    name = models.CharField(max_length=15)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField(max_length=150)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)