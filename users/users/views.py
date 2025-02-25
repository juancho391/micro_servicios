from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class Register(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data.get('username'))
            user.set_password(request.data.get('password'))
            user.save()

            refresh = RefreshToken.for_user(user=user)

            return Response({'message' : 'User Registered succesfully',
                             'status' : status.HTTP_201_CREATED,
                             "Token" : {
                                 "access" : str(refresh.access_token),
                                 "refresh" : str(refresh)
                             },
                             'user' : serializer.data})
        return Response({'message': 'error',
                         'error': serializer.errors,
                         'status': status.HTTP_400_BAD_REQUEST})

class Login(APIView):

    def post(self,request):
        user = get_object_or_404(User, username=request.data.get('username'))
        if not user.check_password(request.data.get('password')):
            return Response({'message':'User or password invalid',
                             'status' : status.HTTP_400_BAD_REQUEST})
        refresh = RefreshToken.for_user(user=user)
        return Response({'message':'login succesfully',
                         'status' : status.HTTP_200_OK,
                          "Token" : {
                                 "access" : str(refresh.access_token),
                                 "refresh" : str(refresh)
                             },
                         'user': UserSerializer(user).data})

#In progress 
class PasswordResetRequest(APIView):
    def post(self,request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({
                'message' : 'Email not Found',
                'status' : status.HTTP_404_NOT_FOUND
            })





    

