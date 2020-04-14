from django.shortcuts import render
from django.views.generic.base import View
from rest_framework.views import APIView
from .serializers import RegistForm, ModifyPasswordForm
from .models import UserProfile, EmailVeriRecord
from rest_framework.response import Response
from rest_framework import status
from utils import email_sender
import base64
import re


class VarifyEmaliView(APIView):
    '''
    验证邮箱
    '''

    def get(self, request):

        q = request.query_params.get('q', '')  # q = 'c=aociegAfpODIRJofO&m=imoocbook@163.com'

        # 解码
        dq = base64.decodebytes(q.encode('utf8'))

        match = re.match(r'c=(.*)&m=(.*)', dq.decode())
        c = match.group(1)
        m = match.group(2)
        try:
            # 获取最新的一条验证码
            instance = EmailVeriRecord.objects.filter(email=m).order_by('-send_time')[0]

            # 验证成功后激活用户
            if instance.code == c :
                user = UserProfile.objects.get(email=instance.email)
                user.is_active = True
                user.save()
                return Response({'msg': '验证成功，用户已激活'}, status=status.HTTP_200_OK)

            return Response({'msg': '验证失败'}, status=status.HTTP_400_BAD_REQUEST)


        except:
            return Response({'msg': 'error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class RegisterView(APIView):
    '''
    注册用户
    '''

    def get(self, request):
        return Response({'msg': "接口调用成功！"}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RegistForm(data=request.data)
        if serializer.is_valid():

            cleaned_email = serializer.validated_data['email']
            if UserProfile.objects.filter(email=cleaned_email, is_active=True):
                # 用户已存在
                return Response({'msg': '用户已存在'}, status=status.HTTP_400_BAD_REQUEST)

            elif UserProfile.objects.filter(email=cleaned_email, is_active=False):
                # 用户提交注册，但未激活
                # 重新发送激活邮件
                try:
                    email_sender.send_email(to_email=cleaned_email, email_type='register')
                    return Response({'msg': '激活码已经发送至邮箱，注意查收'}, status=status.HTTP_201_CREATED)
                except:
                    return Response({'msg': 'error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
