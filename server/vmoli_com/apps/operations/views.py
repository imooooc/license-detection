from django.shortcuts import render
from cars.models import Image, Car
from .serializers import UserCarSerializer
from rest_framework.views import APIView
from .models import UserCar
from rest_framework.response import Response
from rest_framework import status
from django.views.generic.base import View
from django.http import  HttpResponse
# class UserCarList(APIView):
# #     def get(self, request, format=None):
# #         items = UserCar.objects.all()
# #         serialzer = UserCarSerializer(items, many=True)
# #         return Response(serialzer.data, status=status.HTTP_200_OK)

class UserCarList(APIView):
    def get(self, request, format=None):
        items = UserCar.objects.all()
        serializer = UserCarSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

