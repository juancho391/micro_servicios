from django.db import models

# Create your models here.

class Cart(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(default=0)




class CarItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product_name = models.CharField(max_length=100)
    product_id = models.IntegerField(unique=False)
    quantity = models.PositiveIntegerField(default=1)
    product_price = models.IntegerField()





