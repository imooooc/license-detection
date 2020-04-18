# -*- coding:utf-8 -*-
# Author: Zhu Chen 
# Organization: 07 LP detection group
# Create Time: 2020/04  All rights reserved
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    对象级权限，只允许对象的所有者编辑它
    假设模型实例有一个“user”属性
    """

    # 它会来检测我们的obj, 这个obj就是我们从数据库取出来的obj
    def has_object_permission(self, request, view, obj):
        # 读取权限允许任何请求
        # 所以我们总是允许GET、HEAD或OPTIONS请求
        if request.method in permissions.SAFE_METHODS:
            return True

        # 否则我们就判断, 当前数据的用户名是否跟当前用户一致
        # 实例必须有一个名为“user”的属性。
        # model实例obj
        return obj.user == request.user