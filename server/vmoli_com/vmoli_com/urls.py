"""vmoli_com URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import HomeView
from users import urls as users_urls
from cars import urls as cars_urls
from operations import urls as operations_urls
import xadmin

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

]
# hhh