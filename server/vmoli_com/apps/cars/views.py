from django.shortcuts import render
from .models import Car, Image
from rest_framework.decorators import APIView
from .serializers import ImageSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.
class ImageList(APIView):
    def get(self, request, format=None):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request, format=None):
    #     data = request.data
    #     image = Image.objects.create(data)
    #     serializer = ImageSerializer(image)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)


class ImageDetail(APIView):
    def get_object(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data, status=status.HTTP_200_OK)
