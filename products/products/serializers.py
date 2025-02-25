from .models import Product, Category
from rest_framework import serializers



class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id','name','price','stock','description', 'category_name']


    def get_category_name(self,obj):
        return obj.category.name





