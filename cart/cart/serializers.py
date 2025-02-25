from rest_framework import serializers
from .models import Cart, CarItem

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['status', 'created_at', 'total_price']
        read_only_fields = ['created_ad']



class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarItem
        fields = ['cart', 'product_name', 'quantity', 'product_price','product_id']