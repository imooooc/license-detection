# -*- coding:utf-8 -*-# Author: Zhu Chen # Organization: 07 LP detection group# Create Time: 2020/04  All rights reservedfrom .models import UserCarfrom rest_framework import serializersclass UserCarSerializer(serializers.ModelSerializer):    class Meta:        model = UserCar        fields = '__all__'