from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render
from .models import User
from cars.models import Image
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
        imgs = Image.objects.all()[:5]
        ls = serializers.serialize('json', imgs)
        return JsonResponse(json.loads(ls), safe=False)
        pass
    def post(self, request):
        pass