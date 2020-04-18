# -*- coding:utf-8 -*-
# Author: Zhu Chen
# Organization: 07 LP detection group
# Create Time: 2020/04  All rights reserved

from django.shortcuts import render
from .models import Car, Image
from rest_framework.decorators import APIView
from .serializers import ImageSerializer, CarSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from utils.plate_recog_tool import PlateRecogTool
from vmoli_com.settings import BASE_DIR
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from utils.permission import IsOwnerOrReadOnly
from users.models import User

class ImageList(APIView):
    '''
    图片列表
    '''
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def get(self, request, format=None):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # 上传图片后开始进行车牌检测
            image_path = serializer.data.get('source')
            full_path = BASE_DIR + image_path
            print(full_path)
            plate_info = PlateRecogTool(full_path).run()

            # 查询车辆库是否存在该车，存在则更新，若不存在则创建
            # car = Car.objects.get_or_create(plate=plate_info['plate'], defaults=plate_info)
            plate = plate_info.get('plate')
            try:
                car = Car.objects.get(plate=plate)
                car.confidence = plate_info.get('confidence', '')
                car.brand = plate_info.get('brand', '')
                car.color = plate_info.get('color', '')
                car.p1 = plate_info.get('p1', '')
                car.p2 = plate_info.get('p2', '')
                car.p3 = plate_info.get('p3', '')
                car.p4 = plate_info.get('p4', '')
                car.save()
            except Car.DoesNotExist:
                car = Car.objects.create(
                    plate=plate,
                    confidence=plate_info.get('confidence', ''),
                    brand=plate_info.get('brand', ''),
                    color=plate_info.get('color', ''),
                    p1=plate_info.get('p1', ''),
                    p2=plate_info.get('p2', ''),
                    p3=plate_info.get('p3', ''),
                    p4=plate_info.get('p4', ''),
                )

            # 将车辆信息填入该图片记录的car字段
            Image.objects.filter(id=serializer.data.get('id')).update(car=car, user=request.user)

            # 结束后返回data信息和车辆信息
            return Response(plate_info, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDetail(APIView):
    '''
    图片详情
    '''

    def get_object(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = ImageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        image = Image.objects.get(pk=pk)
        image.delete()
        return Response('删除成功', status=status.HTTP_204_NO_CONTENT)


class CarList(APIView):
    '''
    车辆列表
    '''

    def get(self, request, format=None):
        car = Car.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarDetail(APIView):
    '''
    车辆详情
    '''

    def get_object(self, pk):
        try:
            car = Car.objects.get(pk=pk)
            return car
        except Car.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        car = self.get_object(pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
