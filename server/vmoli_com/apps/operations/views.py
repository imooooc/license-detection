# -*- coding:utf-8 -*-
# Author: Zhu Chen
# Organization: 07 LP detection group
# Create Time: 2020/04  All rights reserved

from django.shortcuts import render
from cars.models import Image, Car
from .serializers import UserCarSerializer
from rest_framework.views import APIView
from .models import UserCar
from rest_framework.response import Response
from rest_framework import status
from django.views.generic.base import View
from django.http import HttpResponse
from cars.serializers import CarSerializer, ImageSerializer


class UserCarList(APIView):
    '用户查询车辆历史记录'
    def get(self, request, format=None):
        items = UserCar.objects.filter(user=request.user)
        serializer = UserCarSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = UserCarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Search(APIView):
    '''
    搜索车辆的图片信息
    '''
    def get(self, request, format=None):
        q = request.query_params.get('q', '')
        imgs = Image.objects.filter(car__plate__iexact=q)
        serializer = ImageSerializer(imgs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
