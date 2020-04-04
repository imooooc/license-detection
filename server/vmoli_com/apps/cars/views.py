from django.shortcuts import render
from .models import Car, Image
from rest_framework.decorators import APIView
from .serializers import ImageSerializer, CarSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .plate_recog_tool import PlateRecogTool
from vmoli_com.settings import BASE_DIR
from datetime import datetime


class ImageList(APIView):
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
            tool = PlateRecogTool().run(full_path)
            plate_tool = tool[0][0]
            # 查询车辆库是否存在该车，若不存在则创建
            try:
                car = Car.objects.get(licence_number=plate_tool)
            except Car.DoesNotExist:
                car = Car.objects.create(licence_number=plate_tool, brand="月球车", color="black",
                    create_time=datetime.now())

            # 将车辆信息填入该图
            Image.objects.filter(id=serializer.data.get('id')).update(car=car)

            # 结束后返回data信息
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDetail(APIView):
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
        image = Image.objects.get(pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarList(APIView):
    def get(self, request, format=None):
        car = Car.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarDetail(APIView):
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
