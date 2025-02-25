from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.models import TokenUser

class JWTAuthenticationNoDB(JWTAuthentication):

    def get_user(self,valideated_token):
        return TokenUser(valideated_token)