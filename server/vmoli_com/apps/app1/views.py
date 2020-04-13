from django.shortcuts import render
from django.views.generic.base import View
from rest_framework.views import APIView
from .serializers import RegistForm
from .models import UserProfile, EmailVeriRecord
from rest_framework.response import Response
from rest_framework import status
from utils import email_sender


class EmaliView(View):
    def get(self, request):
        return render(request, 'email.html')


class RegisterView(APIView):
    def get(self, request):
        return Response({'msg': "接口调用成功！"}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RegistForm(data=request.data)
        if serializer.is_valid():

            cleaned_email = serializer.validated_data['email']
            if UserProfile.objects.filter(email=cleaned_email):
                # 用户已存在
                return Response({'msg': '用户已存在'}, status=status.HTTP_400_BAD_REQUEST)

                # 用户名占用
            elif UserProfile.objects.filter(user_name=serializer.validated_data['user_name']):
                return Response({'msg': '用户名被占用'}, status=status.HTTP_400_BAD_REQUEST)

            else:
                # 保存用户信息
                serializer.save()

                # 发送激活邮件
                try:
                    email_sender.send_email(to_email=cleaned_email, email_type='register')
                    return Response({'msg': '激活码已经发送至邮箱，注意查收'}, status=status.HTTP_201_CREATED)
                except:
                    return Response({'msg': 'error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
