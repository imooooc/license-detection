# -*- coding:utf-8 -*-
# Author: Zhu Chen
# Organization: 07 LP detection group
# Create Time: 2020/04  All rights reserved

from django.contrib import admin
from django.urls import path, include
from users.views import HomeView
from users import urls as users_urls
from cars import urls as cars_urls
from operations import urls as operations_urls
import xadmin
from django.conf.urls.static import static
from vmoli_com import settings
from users.views import page_not_found, permission_denied, page_error
import com_static
from rest_framework.authtoken import views as drf_views

urlpatterns = [
                  # 首页
                  path('', HomeView.as_view(), name='home'),

                  # 用户
                  path('u/', include(users_urls), name='users'),

                  # 车辆
                  path('c/', include(cars_urls), name='cars'),

                  # 用户操作
                  path('o/', include(operations_urls), name='operations'),

                  # 后台管理系统
                  path('admin/', xadmin.site.urls),

                  # api管理
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

                  # 颁发token
                  path('api-token-auth/', drf_views.obtain_auth_token)

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error
