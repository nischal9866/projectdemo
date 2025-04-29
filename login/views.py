from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from .serializers import LoginSerializer
# Create your views here.
class LoginAPIView(APIView):
    # serializer_class=LoginSerializer

    @extend_schema(
        request=LoginSerializer,
        responses={201: None},
    )
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        if username==None and password==None:
            raise serializers.ValidationError({
                "details":"Both username and password required"
            })
        user=authenticate(username=username,password=password)
        if user:
            token,_=Token.objects.get_or_create(user=user)
            return Response({
                'token':token.key,
                'user':user.username
            })
        return Response({
            "details":"Username and password is incorrect"
        },status=status.HTTP_401_UNAUTHORIZED)