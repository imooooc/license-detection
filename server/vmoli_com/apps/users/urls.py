from django.conf.urls import url, includefrom django.urls import pathfrom .views import *from rest_framework import routersfrom rest_framework.urlpatterns import format_suffix_patterns# router = routers.DefaultRouter()# router.register(r'user', UserViewSet)urlpatterns = [    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),    path('users/', UserList.as_view()),    path('users/<int:pk>/', UserDetail.as_view()),]urlpatterns = format_suffix_patterns(urlpatterns)