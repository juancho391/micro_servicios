from rest_framework import serializers 
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password','email']
        extra_kwargs = {
            'email' : {'required' : True, 'write_only' : True},
            'password' : {'write_only': True},
        }

    #Validar que no exista un usuario con ese mismo correo
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return value