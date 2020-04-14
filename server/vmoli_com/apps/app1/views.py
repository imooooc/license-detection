from django.shortcuts import render
from django.views.generic.base import View
from rest_framework.views import APIView
from .serializers import RegistForm, ModifyPasswordForm, FrogetPasswordForm
from .models import UserProfile, EmailVeriRecord
from rest_framework.response import Response
from rest_framework import status
from utils import email_sender
import base64
import re
from django.contrib.auth.hashers import make_password, check_password
import random, string


class VerifyEmaliView(APIView):
    '''
    验证邮箱
    '''

    def get(self, request):

        q = request.query_params.get('q', '')  # q = 'c=aociegAfpODIRJofO&m=imoocbook@163.com&t=registerOrforget'

        # 解码
        dq = base64.decodebytes(q.encode('utf8'))

        match = re.match(r'c=(.*)&m=(.*)&t=(.*)', dq.decode())
        c = match.group(1)
        m = match.group(2)
        t = match.group(3)

        # 尝试获取最新的一条验证码
        try:

            instance = EmailVeriRecord.objects.filter(email=m).order_by('-send_time')[0]

            # 核对验证码
            if instance.code == c:
                # 根据不同邮件类型进行相应操作
                # 用户注册
                if t == 'register':
                    user = UserProfile.objects.get(email=instance.email)
                    user.is_active = True
                    user.save()
                    return Response({'msg': '验证成功，用户已激活'}, status=status.HTTP_200_OK)
                # 重置用户密码
                else:
                    user = UserProfile.objects.get(email=instance.email)

                    # 随机生成一个8位数从a-zA-Z0-9的密码,并采用sha1非对称加密保存在数据库
                    _new_password = ''.join(random.sample(string.ascii_letters + string.digits, 8))
                    new_password = make_password(_new_password, 'vmoli', 'pbkdf2_sha1')
                    user.password = new_password
                    user.save()
                    return Response({'msg': '您的密码已重置为{0}，为了您的账号安全，请及时修改密码'.format(_new_password)},
                        status=status.HTTP_205_RESET_CONTENT)

            # 验证失败
            return Response({'msg': '验证失败'}, status=status.HTTP_400_BAD_REQUEST)


        # 验证码不存在
        except EmailVeriRecord.DoesNotExist:
            return Response({'msg': '验证码不存在'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ModifyPasswordView(APIView):
    '''
    修改用户密码;
    user_name:用户名;
    password: 旧密码;
    new_password: 新密码;
    '''

    def get(self, request):

        return Response({'msg': '接口调用成功'}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ModifyPasswordForm(data=request.data)
        if serializer.is_valid():
            # 验证旧密码是否正确
            cleaned_user_name = serializer.validated_data['user_name']
            cleaned_password = serializer.validated_data['password']
            cleaned_new_password = serializer.validated_data['new_password']

            # 查找是否存在该用户
            try:
                user = UserProfile.objects.get(user_name=cleaned_user_name)

                # 与数据库密码匹配判断是否一致
                if check_password(cleaned_password, user.password):
                    user.password = make_password(cleaned_new_password)
                    user.save()
                    return Response({'msg': '密码修改成功'}, status=status.HTTP_205_RESET_CONTENT)
                else:
                    return Response({'msg': '密码错误，请核对'}, status=status.HTTP_400_BAD_REQUEST)

            # 用户不存在，抛出不存在异常异常
            except UserProfile.DoesNotExist:
                return Response({'msg': '该用户不存在'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


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


class ForgetPasswordView(APIView):
    '''
    忘记密码
    email:邮箱
    '''

    def get(self, request):
        return Response({'msg': '接口调用成功'}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FrogetPasswordForm(data=request.data)
        if serializer.is_valid():
            # 如果用户存在
            try:
                user = UserProfile.objects.get(email=serializer.validated_data['email'])

                # 发送验证邮件
                email_sender.send_email(to_email=user.email, email_type='forget')
                return Response({'msg': '验证码已发送至您的邮箱，请注意查收'}, status=status.HTTP_200_OK)

            except UserProfile.DoesNotExist:
                return Response({'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)