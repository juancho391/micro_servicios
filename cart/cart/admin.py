from django.contrib import admin
from .models import Cart, CarItem

# Register your models here.
admin.site.register(CarItem)
admin.site.register(Cart)
