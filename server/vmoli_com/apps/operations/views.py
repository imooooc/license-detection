from django.shortcuts import render
from cars.models import Image, Car
from .serializers import UserCarSerializer
from rest_framework.views import APIView
from .models import UserCar
from rest_framework.response import Response
from rest_framework import status
from django.views.generic.base import View
from django.http import HttpResponse


class UserCarList(APIView):
    def get(self, request, format=None):
        items = UserCar.objects.all()
        serializer = UserCarSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = UserCarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
