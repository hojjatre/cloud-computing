from django.http.response import HttpResponse
from rest_framework import permissions
from django.db.models import F
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework import generics, serializers
from .serializers import UserSerializer
from django.db.models import Avg, Sum, Max, Min
from .models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
import numpy as np
import matplotlib.pyplot as plt
login = obtain_auth_token

class Logout(APIView):
    """
    Delete user's authtoken
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(data={'message': f"Bye {request.user.username}!"}, status=HTTP_204_NO_CONTENT)

class ShowUser(ListAPIView):
    """
    Show users
    """
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

class Register(CreateAPIView):
    """
    Create a new user
    """
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer