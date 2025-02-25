from django.shortcuts import render
from .models import CarItem, Cart
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartItemSerializer
from .authentication import JWTAuthenticationNoDB
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import requests


# Create your views here.

class ItemToCart(APIView):
    # authentication_classes = [JWTAuthenticationNoDB]
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        item_id = request.data.get('product_id')
        cart_id = request.data.get('cart')
        #obtenemos el carrito
        cart,cart_created = Cart.objects.get_or_create(id=cart_id)

        #Verificamos si el producto ya existe
        if CarItem.objects.filter(product_id=item_id, cart_id=cart_id).exists():
            return Response({
                'message': 'Error this product already exist',
                'status': status.HTTP_400_BAD_REQUEST
            })
        
        #si no existe creamos un nuevo CarItem
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #actualizamos el precio total del carrito 
            cart.total_price +=  request.data.get('product_price') * request.data.get('quantity')
            cart.save()
            return Response({
                    'message': 'Product added successfully',
                    'product': serializer.data  
                })
        
        return Response({
                'message': 'Error this product already exist',
                'status': status.HTTP_400_BAD_REQUEST,
                'error' : serializer.errors
            })

    
    def delete(self,request):
        item_id = requests.data.get('item_id')
        cart_id = requests.data.get('cart_id')
        #Obtenemos el carrito al que pertenece el producto 
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            return Response({
                "Message" : "Car Not Found",
            })
        try:
            #Obtenemos el item 
            cart_item = CarItem.objects.get(product_id=item_id,cart_id=cart_id)
        except CarItem.DoesNotExist:
            return Response({
                "Message" : "Item Not Found"
            })
        if cart_item.quantity == 1:
            price = cart_item.product_price * cart_item.quantity
            cart.total_price -= price
            cart.save()
            cart_item.delete()
            items = CarItem.objects.filter(cart=cart_id)
            serializer = CartItemSerializer(items,many=True)
            return Response({
                "message" : "Product Delete",
                "Items" : serializer.data,
                f"total price" : cart.total_price 
            })
        else:
            cart_item.quantity -= 1
            cart.total_price -= cart_item.product_price
            cart_item.save()
            cart.save()
            items = CarItem.objects.filter(cart=cart_id)
            serializer = CartItemSerializer(items,many=True)
            return Response({
                "message" : "One Product Update",
                "Items" : serializer.data,
                f"total price" : cart.total_price 
            })
        
    
    def put(self,request):
        item_id = request.data.get('item_id')
        cart_id = request.data.get('cart_id')
        #Obtenemos el carrito al que pertenece el producto 
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            return Response({
                "Message" : "Car Not Found",
            })
        try:
            #Obtenemos el item 
            cart_item = CarItem.objects.get(product_id=item_id,cart_id=cart_id)
        except CarItem.DoesNotExist:
            return Response({
                "Message" : "Item Not Found"
            })
        cart_item.quantity += 1
        cart.total_price += cart_item.product_price
        cart.save()
        cart_item.save()
        items = CarItem.objects.filter(cart_id=cart_id)
        serializer = CartItemSerializer(items,many=True)
        return Response({
                "message" : "One Product Update",
                "Items" : serializer.data,
                f"total price" : cart.total_price 
            })
        

class GetItemsOfCart(APIView):
    # authentication_classes = [JWTAuthenticationNoDB]
    # permission_classes = [IsAuthenticated]
    def get(self,request,cart_id):
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            return Response({
                "message" : "Cart Not Found",
                "status" : status.HTTP_404_NOT_FOUND
            })
        items = CarItem.objects.filter(cart_id=cart_id)        
        serializer = CartItemSerializer(items, many=True)
        return Response({
            "items": serializer.data,
            f"total_price_cart" : cart.total_price,
            "status": status.HTTP_200_OK
        })
    


class GetProducts(APIView):
    
    def get(self,request):
        try:
            response = requests.get("http://products:8000/products")
        except ValueError:
            return Response({
                "Message": "Error in the request"
            })
        
        print(response.json())
        
        return Response({
            "Message" : "request succesfully",
            "response" : response.json()
        })


    