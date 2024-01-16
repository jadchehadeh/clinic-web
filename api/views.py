from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer

class UserGetCreate(generics.ListCreateAPIView): #Class Based View Api Responsible to Retrieve all data from the database Todo and uses the serializer class TodoSerlialiazer#
    queryset=User.objects.all()
    serializer_class= UserSerializer

# Create your views here.
