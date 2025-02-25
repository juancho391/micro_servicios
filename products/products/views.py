from django.shortcuts import render
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .authentication import JWTAuthenticationNoDB


# Create your views here.

class ListProducts(APIView):
    # authentication_classes = [JWTAuthenticationNoDB]
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({
            'status' : status.HTTP_200_OK,
            'products' : serializer.data,
        })
    

class ProductDetail(APIView):
    # authentication_classes = [JWTAuthenticationNoDB]
    # permission_classes = [IsAuthenticated]

    def get(self,request, pk):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response(
                {'status': status.HTTP_404_NOT_FOUND,
                 'message': f'Product {pk} not found'}
            )
        
        serializer = ProductSerializer(product)
        return Response(
            {'status':status.HTTP_200_OK,
             'product': serializer.data}
        )
    
class FilterProductsByPrice(APIView):
    # authentication_classes = [JWTAuthenticationNoDB]
    # permission_classes = [IsAuthenticated]
    def get(self, request, price):
        # Filtrando productos por precio
        products = Product.objects.filter(price__gt=price)
        
        # Verificar si se encontraron productos
        if not products.exists():
            return Response(
                {'status': status.HTTP_404_NOT_FOUND,
                 'message': f'There are no products with the price {price}'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Serializar los productos encontrados
        serializer = ProductSerializer(products, many=True)
        return Response(
            {'status': status.HTTP_200_OK, 
             'products': serializer.data},
            status=status.HTTP_200_OK
        )

class GetProductsByName(APIView):
    # authentication_classes = [JWTAuthenticationNoDB]
    # permission_classes = [IsAuthenticated]

    def get(self,request,name):
        products = Product.objects.filter(name=name)


        if not products.exists():
            return Response(
                {'status': status.HTTP_404_NOT_FOUND,
                 'message': f'Product Not Found'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ProductSerializer(products, many=True)
        return Response(
            {'status': status.HTTP_200_OK, 
             'products': serializer.data},
            status=status.HTTP_200_OK
        )

class GetProductsByCategory(APIView):
    # authentication_classes = [JWTAuthenticationNoDB]
    # permission_classes = [IsAuthenticated]
    def get(self,request, category_name:str):
        category_name = category_name.capitalize()
        print(category_name)
        category = Category.objects.get(name=category_name)
        products = Product.objects.filter(category=category.id)
        if not products.exists():
            return Response(
                {'status': status.HTTP_404_NOT_FOUND,
                 'message': f'Products of category {category_name} not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = ProductSerializer(products, many=True)
        return Response(
            {'status': status.HTTP_200_OK, 
             'products': serializer.data},
            status=status.HTTP_200_OK
        )



