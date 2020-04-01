from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render
from .models import User
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class UserView(View):
    def get(self, request):
        res = request
        imgs = User.objects.all()[:5]
        ls = serializers.serialize('json', imgs)
        return JsonResponse(json.loads(ls), safe=False)
        pass
    def post(self, request):
        # openid = models.CharField(max_length=100, verbose_name=u'openid', primary_key=True)
        # stu_id = models.CharField(max_length=10, verbose_name=u'学号', default='')
        # pwd = models.CharField(max_length=20, verbose_name=u'密码', null=True, blank=True)
        # name = models.CharField(max_length=20, verbose_name=u'姓名', default='nobody')
        # create_time
        # openid = '001'
        pass
