# -*- coding:utf-8 -*-# Author: Zhu Chen # Organization: 07 LP detection group# Create Time: 2020/04  All rights reservedfrom rest_framework import serializersfrom .models import UserProfilefrom django.contrib.auth.hashers import make_password, check_passwordclass RegistForm(serializers.Serializer):    user_name = serializers.CharField(required=True, max_length=20)    email = serializers.EmailField(required=True, max_length=50)    password = serializers.CharField(required=True, max_length=256)    re_password = serializers.CharField(required=True, max_length=256)    # data = {'user_name':'张三', 'email':'1@1.com', 'password':'123', 're_password':'123'}    def validate(self, attrs):        if attrs['password'] != attrs['re_password']:            raise serializers.ValidationError('两次密码输入不一致')        return attrs    def save(self):        data = {}        user_name = self.validated_data['user_name']        email = self.validated_data['email']        _password = self.validated_data['password']        # sha1非对称加密保存密码        password = make_password(_password, 'vmoli', 'pbkdf2_sha1')        print('data:', data)        return UserProfile.objects.create(user_name=user_name, email=email, password=password)class ModifyPasswordForm(serializers.Serializer):    user_name = serializers.CharField(required=True, max_length=20)    password = serializers.CharField(required=True, max_length=256)    new_password = serializers.CharField(required=True, max_length=256)    def validate(self, attrs):        if attrs['password'] == attrs['new_password']:            raise serializers.ValidationError('新密码不能和旧密码相同')        return attrsclass FrogetPasswordForm(serializers.Serializer):    email = serializers.EmailField(required=True, max_length=50)